#!/usr/bin/env python3

from redisc import get_redis
from mongo import get_mongo
from models import get_version

r_conn = get_redis()
db = get_mongo()
models = get_version(1)