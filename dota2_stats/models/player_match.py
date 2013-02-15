from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from dota2_stats.models.base import Base


class PlayerMatch(Base):
    __tablename__ = 'player_match'
    id = Column(BigInteger, primary_key=True)
    player_id = Column(BigInteger, ForeignKey('player.id'), nullable=True)
    match_id = Column(BigInteger, ForeignKey('match.id'))
    hero_id = Column(Integer, ForeignKey('hero.id'))
    is_dire = Column(Boolean)
    slot = Column(Integer)

    item_slot_0 = Column(Integer, ForeignKey('item.id'), nullable=True)
    item_slot_1 = Column(Integer, ForeignKey('item.id'), nullable=True)
    item_slot_2 = Column(Integer, ForeignKey('item.id'), nullable=True)
    item_slot_3 = Column(Integer, ForeignKey('item.id'), nullable=True)
    item_slot_4 = Column(Integer, ForeignKey('item.id'), nullable=True)
    item_slot_5 = Column(Integer, ForeignKey('item.id'), nullable=True)

    kills = Column(Integer)
    deaths = Column(Integer)
    assists = Column(Integer)

    abandoned = Column(Boolean)

    gold = Column(Integer)
    last_hits = Column(Integer)
    denies = Column(Integer)
    gold_per_min = Column(Integer)
    xp_per_min = Column(Integer)
    gold_spent = Column(Integer)
    hero_damage = Column(Integer)
    tower_damage = Column(Integer)
    hero_healing = Column(Integer)
    level = Column(Integer)

    player = relationship('Player', backref='matches', lazy='joined')
    match = relationship('Match', backref='player_matches', lazy='joined')
    hero = relationship('Hero', backref='matches', lazy='joined')

    item_0 = relationship('Item', foreign_keys=[item_slot_0])
    item_1 = relationship('Item', foreign_keys=[item_slot_1])
    item_2 = relationship('Item', foreign_keys=[item_slot_2])
    item_3 = relationship('Item', foreign_keys=[item_slot_3])
    item_4 = relationship('Item', foreign_keys=[item_slot_4])
    item_5 = relationship('Item', foreign_keys=[item_slot_5])

    @property
    def items(self):
        return [
                self.item_0,
                self.item_1,
                self.item_2,
                self.item_3,
                self.item_4,
                self.item_5,
            ]

    @property
    def url(self):
        return '/players/{}'.format(self.id)

    def __repr__(self):
        return '<PlayerMatch id={} player_id={} match_id={}>'.format(
                self.id, self.player_id, self.match_id)

