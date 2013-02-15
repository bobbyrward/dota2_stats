import json

from pyramid.httpexceptions import HTTPSeeOther
from pyramid.view import view_config

from dota2_stats.api_client import convert_player_id_64_to_32
from dota2_stats.models import DBSession
from dota2_stats.models import Player


@view_config(
    context='velruse.AuthenticationComplete',
    renderer='templates/login_result.jinja2'
)
def on_login_success(request):
    context = request.context

    steam_url = context.profile['accounts'][0]['username']
    steam_id = convert_player_id_64_to_32(long(steam_url.rsplit('/', 1)[1]))

    player = DBSession.query(Player).get(steam_id)

    if player is not None:
        player.is_registerd = True
    else:
        player = Player(id=steam_id, is_registerd=True)
        DBSession.add(player)

    request.session['current_player_steamid'] = steam_id
    request.session['current_player'] = player

    return HTTPSeeOther(location='/')


@view_config(
    context='velruse.AuthenticationDenied',
    renderer='templates/login_result.jinja2'
)
def on_login_failure(request):
    return HTTPSeeOther(location='/')
