import logging
from datetime import datetime

import transaction
from dateutil.tz import tzutc

from dota2_stats import api_client
from dota2_stats.api_client import get_player_list_details
from dota2_stats.api_client import convert_player_id_32_to_64
from dota2_stats.api_client import convert_player_id_64_to_32
from dota2_stats.models import DBSession
from dota2_stats.models import Hero
from dota2_stats.models import Item
from dota2_stats.models import Match
from dota2_stats.models import Player
from dota2_stats.models import PlayerMatch
from dota2_stats.tasks.common import celery

log = logging.getLogger(__name__)


@celery.task()
def update_players_matches():
    pass


@celery.task()
def update_recent_matches():
    result = api_client.get_match_history(celery.settings)

    for match in result['matches']:
        with transaction.manager:
            if match['match_id'] is None:
                continue

            if DBSession.query(Match).get(match['match_id']):
                continue

            db_match = Match(
                id=match['match_id'],
                start_time=datetime.fromtimestamp(int(match['start_time']), tzutc()),
                lobby_type=match['lobby_type'],
            )

            log.info('Adding new match: id={}'.format(db_match.id))

            for player in match['players']:
                db_player = None

                if 'account_id' in player:
                    db_player = DBSession.query(Player).get(player['account_id'])

                    if not db_player:
                        db_player = Player(id=player['account_id'])
                        log.info('Adding new player: id={}'.format(db_player.id))

                slot = int(player['player_slot'])

                is_dire = slot & 0x80
                slot &= ~0x80

                db_player_match = PlayerMatch(
                        player=db_player,
                        match=db_match,
                        hero=DBSession.query(Hero).get(player['hero_id']),
                        is_dire=bool(is_dire),
                        slot=slot,
                    )

                log.info('Adding new player match: id={}'.format(db_player_match.id))

                DBSession.add(db_match)

                update_match_details.apply_async((db_match.id,))

    update_player_details.apply_async()


@celery.task()
def update_match_details(match_id):
    with transaction.manager:
        log.info('Getting match details for match {}'.format(match_id))

        match = DBSession.query(Match).get(match_id)
        result = api_client.get_match_details(celery.settings, match_id)

        log.debug('Result = {}'.format(result))

        copy_entry = lambda name: setattr(match, name, result[name])
        translate_entry = lambda name, name_response: setattr(match, name, result[name_response])

        match.radiant_win = (result['radiant_win'] == 'True')

        copy_entry('duration')
        copy_entry('tower_status_radiant')
        copy_entry('tower_status_dire')
        copy_entry('barracks_status_radiant')
        copy_entry('barracks_status_dire')
        copy_entry('cluster')
        copy_entry('first_blood_time')
        #copy_entry('replay_salt')
        translate_entry('num_human_player', 'human_players')
        translate_entry('league_id', 'leagueid')
        copy_entry('positive_votes')
        copy_entry('negative_votes')

        for player in result['players']:
            log.info('Looking up player {} in match {} in slot {} on {}'.format(
                    match_id,
                    player['account_id'],
                    player['player_slot'] & ~0x80,
                    'DIRE' if player['player_slot'] & 0x80 else 'RADIANT',
                ))

            pm = DBSession.query(PlayerMatch).filter_by(
                    match_id=match_id,
                    player_id=player['account_id'],
                    slot=player['player_slot'] & ~0x80,
                    is_dire=(player['player_slot'] & 0x80 == 0x80),
                ).one()

            def update_item_slot(slot_num):
                if player['item_{}'.format(slot_num)] != 0:
                    item = DBSession.query(Item).get(player['item_{}'.format(slot_num)])

                    log.info('Player has item #{}, {} in slot {}'.format(
                        player['item_{}'.format(slot_num)],
                        item.name,
                        slot_num,
                    ))

                    setattr(pm, 'item_{}'.format(slot_num), item)
                else:
                    setattr(pm, 'item_{}'.format(slot_num), None)


            update_item_slot(0)
            update_item_slot(1)
            update_item_slot(2)
            update_item_slot(3)
            update_item_slot(4)
            update_item_slot(5)

            pm.kills = player['kills']
            pm.deaths = player['deaths']
            pm.assists = player['assists']

            pm.abandoned = (player['leaver_status'] == 1)

            pm.gold = player['gold']
            pm.last_hits = player['last_hits']
            pm.denies = player['denies']
            pm.gold_per_min = player['gold_per_min']
            pm.xp_per_min = player['xp_per_min']
            pm.gold_spent = player['gold_spent']
            pm.hero_damage = player['hero_damage']
            pm.tower_damage = player['tower_damage']
            pm.hero_healing = player['hero_healing']
            pm.level = player['level']


@celery.task()
def update_player_details():
    with transaction.manager:
        while True:
            players = DBSession.query(Player).filter_by(display_name=None,
                    profile_update_error=False).limit(100).all()

            if not players:
                log.info('All player details up to date')
                break

            player_ids = [
                str(convert_player_id_32_to_64(player.id))
                    for player in players if player.id != 4294967295
            ]

            log.info('Updating player details for {} players'.format(len(player_ids)))

            result = get_player_list_details(celery.settings, player_ids)

            for player in result['players']:
                id_32 = convert_player_id_64_to_32(long(player['steamid']))

                log.info('Updating player {}'.format(id_32))

                db_player = DBSession.query(Player).get(id_32)
                db_player.display_name = player['personaname']
                players.remove(db_player)

            if players:
                log.info('Player not updated: {}'.format(len(players)))

                for player in players:
                    player.profile_update_error = True

