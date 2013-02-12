from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from dota2_stats.models.base import DBSession
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


class Player(Base):
    __tablename__ = 'player'
    id = Column(BigInteger, primary_key=True)
    display_name = Column(String(250), nullable=True)
    profile_update_error = Column(Boolean, default=False)

    @property
    def is_anonymous(self):
        return self.id == 4294967295

    @property
    def url(self):
        return '/players/{}'.format(self.id)

    def __repr__(self):
        return '<Player id={} display_name={}>'.format(self.id, self.display_name)


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
