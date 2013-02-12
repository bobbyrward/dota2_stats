import requests
import json


MAGIC_STEAMID_CONVERSION = 76561197960265728L


def get_heroes(settings):
    response = requests.get('https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/',
            params={'key': settings['steam.api_key'], 'language': 'en'})

    response.raise_for_status()

    return json.loads(response.content)['result']


def convert_player_id_32_to_64(player_id_32bit):
    return player_id_32bit + MAGIC_STEAMID_CONVERSION


def convert_player_id_64_to_32(player_id_64bit):
    return player_id_64bit - MAGIC_STEAMID_CONVERSION


def get_player_list_details(settings, list_player_ids):
    response = requests.get(
            'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/',
            params={'steamids': ','.join(list_player_ids + ['']), 'key': settings['steam.api_key']})

    response.raise_for_status()

    return json.loads(response.content)['response']


def get_player_details(settings, player_id_32bit):
    return get_player_list_details(settings, [player_id_32bit])


def get_match_history(settings):
    response = requests.get('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/',
            params={'key': settings['steam.api_key']})

    response.raise_for_status()

    return json.loads(response.content)['result']


def get_match_details(settings, match_id):
    response = requests.get('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/',
            params={'key': settings['steam.api_key'], 'match_id': match_id})

    response.raise_for_status()

    return json.loads(response.content)['result']
