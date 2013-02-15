from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from dota2_stats.models.base import Base


class Match(Base):
    __tablename__ = 'match'
    id = Column(BigInteger, primary_key=True)
    start_time = Column(DateTime(timezone=True))
    lobby_type = Column(Integer)  # TODO: Make this a foreign key to a new table

    radiant_win = Column(Boolean)
    duration = Column(Integer)
    tower_status_radiant = Column(Integer)
    tower_status_dire = Column(Integer)
    barracks_status_radiant = Column(Integer)
    barracks_status_dire = Column(Integer)
    cluster = Column(String(250))
    first_blood_time = Column(Integer)
    replay_salt = Column(String(250))
    num_human_player = Column(Integer)
    league_id = Column(Integer)
    positive_votes = Column(Integer)
    negative_votes = Column(Integer)

    dire_players = relationship('PlayerMatch', order_by='PlayerMatch.slot',
            primaryjoin="and_(PlayerMatch.match_id == Match.id, PlayerMatch.is_dire == 'true')",
            lazy='joined')

    radiant_players = relationship('PlayerMatch', order_by='PlayerMatch.slot',
            primaryjoin="and_(PlayerMatch.match_id == Match.id, PlayerMatch.is_dire == 'false')",
            lazy='joined')

    def __repr__(self):
        return '<Match id={}>'.format(self.id)

    @property
    def url(self):
        return '/matches/{}'.format(self.id)

    @property
    def duration_string(self):
        if self.duration is None:
            return '00:00'

        return '{:02d}:{:02d}'.format(
                self.duration % 60,
                self.duration / 60,
            )



