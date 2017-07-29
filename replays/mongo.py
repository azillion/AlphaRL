#!/usr/bin/env python3

from os import environ
from socket import gethostbyname

from mongoengine import connect

_mongo_singleton = None

_DEFAULT_MONGO_HOST = 'localhost'
_DEFAULT_MONGO_DB = 'ReplayIndex'


def create_mongo(mongo_host: str, mongo_db: str):
    """Create the mongo connection"""
    mongo_ip = gethostbyname(mongo_host)
    mongo_user = environ["MONGO_USERNAME"]
    mongo_pass = environ["MONGO_PASS"]
    print(f"Mongo IP: {mongo_ip}")
    print(f"Mongo Host: {mongo_host}")
    print(f"Mongo Database: {mongo_db}")
    print(f"Mongo Username: {mongo_user}")
    return connect(mongo_db, host=mongo_ip, \
                    username=mongo_user, password=mongo_pass, authentication_source="admin")
    


def get_mongo():
    """Returns the mongo database singleton"""
    global _mongo_singleton
    mongo_host = environ.get('MONGO_HOST', _DEFAULT_MONGO_HOST)
    mongo_db = environ.get('MONGO_DB', _DEFAULT_MONGO_DB)
    
    if _mongo_singleton is None:
        _mongo_singleton = create_mongo(mongo_host, mongo_db)
    print(_mongo_singleton)
    return _mongo_singleton
