from pyramid.view import view_config

from dota2_stats.models import DBSession
from dota2_stats.models import Player
from dota2_stats.views.common import template_params


@view_config(route_name='players_index', renderer='templates/players.jinja2')
def players_index(request):
    return template_params(request)


@view_config(route_name='player_details', renderer='templates/player_details.jinja2')
def player_details(request):
    player = DBSession.query(Player).filter_by(id=request.matchdict['id']).one()
    return template_params(request, player=player)
