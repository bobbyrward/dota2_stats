from pyramid.view import view_config

from dota2_stats.views.heroes import all_heroes
from dota2_stats.views.items import all_items
from dota2_stats.views.matches import recent_matches
from dota2_stats.views.matches import match_details
from dota2_stats.views.auth import on_login_success
from dota2_stats.views.auth import on_login_failure


@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'settings': request.registry.settings}
