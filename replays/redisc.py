#!/usr/bin/env python3

from os import environ

import redis

_redis_singleton = None

_DEFAULT_REDIS_HOST = 'localhost'
_DEFAULT_REDIS_PORT = '6379'
_DEFAULT_REDIS_DB = 0


def create_redis(redis_host: str, redis_port: int, redis_db: int) -> redis.connection():
    """Create the redis connection"""
    print(f"Redis Host: {redis_host}")
    print(f"Redis Port: {redis_port}")
    print(f"Redis Database: {redis_db}")
    return redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
    


def get_redis():
    """Returns the redis singleton"""
    global _redis_singleton
    redis_host = environ.get('REDIS_HOST', _DEFAULT_REDIS_HOST)
    redis_port = environ.get('REDIS_PORT', _DEFAULT_REDIS_PORT)
    redis_db = environ.get('REDIS_DB', _DEFAULT_REDIS_DB)
    
    if _redis_singleton is None:
        _redis_singleton = create_redis(redis_host, redis_port, redis_db)
    print(_redis_singleton)
    return _redis_singleton
