from pyramid.view import view_config

from sqlalchemy.sql import not_

from dota2_stats.models import DBSession
from dota2_stats.models import Item


@view_config(route_name='items', renderer='templates/items.jinja2')
def all_items(request):
    items = DBSession.query(Item).filter(not_(Item.name.startswith('item_recipe_'))).order_by('id').all()
    return {'items': items}



