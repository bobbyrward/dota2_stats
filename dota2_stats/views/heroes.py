from pyramid.view import view_config

from dota2_stats.models import DBSession
from dota2_stats.models import Hero
from dota2_stats.views.common import template_params


@view_config(route_name='heroes', renderer='templates/heroes.jinja2')
def all_heroes(request):
    heroes = DBSession.query(Hero).order_by('id').filter(Hero.released == True).all()
    return template_params(request, heroes=heroes)


@view_config(route_name='hero_details', renderer='templates/hero_details.jinja2')
def hero_details(request):
    name = 'npc_dota_hero_{}'.format(request.matchdict['name'].replace('-', '_'))
    hero = DBSession.query(Hero).filter_by(name=name).one()
    return template_params(request, hero=hero)
