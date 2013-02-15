from pyramid.view import view_config

from dota2_stats.models import DBSession
from dota2_stats.views.common import template_params


@view_config(route_name='trends_index', renderer='templates/trends.jinja2')
def trends_index(request):
    return template_params(request)

