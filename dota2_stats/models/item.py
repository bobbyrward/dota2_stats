from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from dota2_stats.models.base import Base


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)

    @property
    def url(self):
        return '/items/{}'.format(self.name[5:])

    @property
    def thumbnail_image_url(self):
        return '/static/img/items/small/{}.png'.format(self.name.replace('recipe_', ''))

    @property
    def full_image_url(self):
        return '/static/img/items/{}.png'.format(self.name.replace('recipe_', ''))

    def __repr__(self):
        return '<Item id={} name={}>'.format(self.id, self.name)



