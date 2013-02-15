from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from dota2_stats.models.base import Base


class Hero(Base):
    __tablename__ = 'hero'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)
    proper_name = Column(String(250), unique=True)
    released = Column(Boolean, default=True)

    @property
    def url(self):
        return '/heroes/{}'.format(self.name[14:].replace('_', '-'))

    @property
    def vertical_image_url(self):
        return '/static/img/heroes/{}.png'.format(self.name)

    @property
    def large_image_url(self):
        return '/static/img/heroes/valve/{}_full.png'.format(self.name[14:])

    @property
    def thumbnail_image_url(self):
        return '/static/img/heroes/valve/{}_sb.png'.format(self.name[14:])

    def __repr__(self):
        return '<Hero id={} name={}>'.format(self.id, self.name)



