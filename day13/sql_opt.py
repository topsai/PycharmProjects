#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:123456@192.168.100.5/test",
                       encoding='utf-8', echo=False)
Base = declarative_base()  # 生成orm基类

class Server_info(Base):
    __tablename__ = 'server_info'
    id = Column(Integer, primary_key=True)
    server_name = Column(String(64))
    server_ip = Column(String(64))
    server_port = Column(Integer)
    server_pwd = Column(String(128))
    server_key = Column(String(128))

class Server_group(Base):
    __tablename__ = 'server_group'
    id = Column(Integer, primary_key=True)
    server_id = Column(Integer, ForeignKey('server_info.id'))
    group_id = Column(Integer, ForeignKey('group_info.id'))

class User_info(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(64))
    user_pwd = Column(String(128))

class User_group(Base):
    __tablename__ = 'user_group'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_info.id'))
    group_id = Column(Integer, ForeignKey('group_info.id'))

class Group_info(Base):
    __tablename__ = 'group_info'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(64))

Base.metadata.create_all(engine)
