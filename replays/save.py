#!/usr/bin/env python3
from time import sleep
from pathlib import Path

import requests
import requests_cache

from replays.mongo import get_mongo
from replays.models import get_version

db = get_mongo()
models = get_version(1)

requests_cache.install_cache('files_requests')

def save(file_url):
    if file_url is None:
        return False
    try:
        path = Path("encoded").resolve()
        file_name = file_url.replace("https://media.rocketleaguereplays.com/uploads/replay_files/", "")
        path = path / file_name
        r = requests.get(file_url, stream=True)

        if not r.ok:
            r.raise_for_status()

        with open(path, 'wb') as file:
            for block in r.iter_content(2000):
                file.write(block)
        return True
    except Exception as e:
        print(e)
        return False