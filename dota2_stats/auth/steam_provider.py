"""An attempt at a steam open id provider for velruse

I got distracted with other things.  No idea if this really works
"""
import logging

from openid.extensions import ax
from openid.extensions import sreg
from pyramid.security import NO_PERMISSION_REQUIRED

from velruse.api import register_provider
from velruse.providers.openid import attributes
from velruse.providers.openid import OpenIDAuthenticationComplete
from velruse.providers.openid import OpenIDConsumer


log = logging.getLogger(__name__)


def register_steam_provider(config):
    provider = SteamOpenIDConsumer(
        'steam',
        None,
        'http://ohnozombi.es/',
        None,
    )

    config.add_route(provider.login_route, '/login/steam/')
    config.add_view(provider, attr='login', route_name=provider.login_route,
                    permission=NO_PERMISSION_REQUIRED)

    config.add_route(provider.callback_route, '/login/steam/callback/',
                     use_global_views=True,
                     factory=provider.callback)

    register_provider(config, 'steam', provider)


class SteamOpenIDConsumer(OpenIDConsumer):
    def __init__(self, name, attrs=None, realm=None, storage=None):
        """Handle Google Auth

        This also handles making an OAuth request during the OpenID
        authentication.

        """
        OpenIDConsumer.__init__(self, name, 'steam_openid', realm, storage)

        if attrs is not None:
            self.openid_attributes = attrs

    def _lookup_identifier(self, request, identifier):
        """Return the Google OpenID directed endpoint"""
        return "http://steamcommunity.com/openid"
