from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import relationship

from dota2_stats.models.base import Base


class Player(Base):
    __tablename__ = 'player'
    id = Column(BigInteger, primary_key=True)
    display_name = Column(String(250), nullable=True)
    profile_update_error = Column(Boolean, default=False)
    is_registerd = Column(Boolean, default=False)
    last_updated = Column(DateTime(timezone=True), nullable=True)

    @property
    def is_anonymous(self):
        return self.id == 4294967295

    @property
    def url(self):
        return '/players/{}'.format(self.id)

    def __repr__(self):
        return '<Player id={} display_name={}>'.format(self.id, self.display_name)
