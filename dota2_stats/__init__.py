from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from sqlalchemy import engine_from_config
from dota2_stats.auth.steam_provider import register_steam_provider

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = UnencryptedCookieSessionFactoryConfig(
        'meepown3d'
    )
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.set_session_factory(session_factory)
    config.add_route('index', r'/')
    config.add_route('items', r'/items')
    config.add_route('heroes', r'/heroes')
    config.add_route('hero_details', r'/heroes/{name:[\w\-]+}')
    config.add_route('recent_matches', r'/matches')
    config.add_route('match_details', r'/matches/{id:\d+}')
    config.add_route('players_index', r'/players')
    config.add_route('player_details', r'/players/{id:\d+}')
    config.add_route('trends_index', r'/trends')
    config.include('velruse.providers.openid')
    config.add_openid_login('ohnozombi.es')
    register_steam_provider(config)
    config.scan()
    return config.make_wsgi_app()
