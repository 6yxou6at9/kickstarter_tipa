from tkinter.constants import CASCADE

from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    phone_number = Column(String)
    password = Column(String, nullable=False)
    reg_time = Column(DateTime, default=datetime.now)

    campaign_fk = relationship('Campaign', back_populates='user_fk', cascade='all, delete-orphan')
    comment_fk = relationship('Comment', back_populates='user_fk', cascade='all, delete-orphan')
    transfer_fk = relationship('Transfer', back_populates='campaign_fk', cascade='all, delete-orphan')

class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    expected_sum = Column(Integer, nullable=False)
    sum_now = Column(Integer, default=0)
    campaign_owner_user_id = Column(Integer, ForeignKey('users.id', ondelete=CASCADE))
    expected_sum_achieved = Column(Boolean, default=False)

    user_fk = relationship('User', back_populates='campaign_fk', lazy='joined')
    comment_fk = relationship('Comment', back_populates='campaign_fk', cascade='all, delete-orphan')
    transfer_fk = relationship('Transfer', back_populates='campaign_fk', cascade='all, delete-orphan')


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, autoincrement=True, primary_key=True)
    comment_user_id = Column(Integer, ForeignKey('users.id', ondelete=CASCADE))
    comment_campaign_id = Column(Integer, ForeignKey('campaigns.id', ondelete=CASCADE))
    text = Column(String, nullable=False)

    campaign_fk = relationship('Campaign', back_populates='comment_fk', lazy='joined')
    user_fk = relationship('User', back_populates='comment_fk', lazy='joined')


class Transfer(Base):
    __tablename__ = 'transfers'

    id = Column(Integer, autoincrement=True, primary_key=True)
    transfer_campaign_id = Column(Integer, ForeignKey('campaigns.id', ondelete=CASCADE))
    transfer_user_id = Column(Integer, ForeignKey('users.id', ondelete=CASCADE))
    summ = Column(Integer, nullable=False)

    campaign_fk = relationship('Campaign', back_populates='transfer_fk', lazy='joined')
    user_fk = relationship('User', back_populates='transfer_fk', lazy='joined')