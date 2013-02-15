from pyramid.view import view_config

from dota2_stats.models import DBSession
from dota2_stats.models import Match
from dota2_stats.models import PlayerMatch
from dota2_stats.models import Player
from dota2_stats.models import Hero
from dota2_stats.views.common import template_params


@view_config(route_name='recent_matches', renderer='templates/recent_matches.jinja2')
def recent_matches(request):
    matches = DBSession.query(Match).order_by(Match.start_time.desc()).limit(25).all()
    return template_params(request, matches=matches)


@view_config(route_name='match_details', renderer='templates/match_details.jinja2')
def match_details(request):
    match = DBSession.query(Match).get(request.matchdict['id'])
    return template_params(request, match=match)
