 #!/usr/bin/env python3

import json
from sys import exit
from time import sleep
from pathlib import Path

import requests
import requests_cache

from replays.mongo import get_mongo
from replays.models import get_version
from replays.save import save

db = get_mongo()
models = get_version(1)

"""TODO:
    - Save all results to a mongo database
    - Retrieve all replays
    - Parse all replays
    - Store all replay data in separate mongo database
"""

requests_cache.install_cache('replay_requests')


def main():
    delay = 0.5
    count = 1
    url = "https://www.rocketleaguereplays.com/api/replays/"
    r = requests.get(url)
    
    if not r.ok:
        exit(f"Initial request failed.\nResponse Code {r.status_code}")

    for f in r.json().get('results', []):
        file_url = f.get('file', None)
        # f_r = save(file_url)
        # if f_r is False:
            # print(f"Failed to retrieve {file_url}")

    next_url = r.json().get('next', False)
    while next_url is not False:
        print("Page ", count)
        count += 1
        r = requests.get(next_url)
        while not r.ok:
            if delay > 1800:
                exit("Throttled too hard")
            sleep(delay)
            delay *= 1.5
            r = requests.get(next_url)

        for f in r.json().get('results', []):
            file_url = f.get('file', None)
            # f_r = save(file_url)
            # if f_r is False:
                # print(f"Failed to retrieve {file_url}")

        next_url = r.json().get('next', False)


if __name__ == "__main__":
    main()
