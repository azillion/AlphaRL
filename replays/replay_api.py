 #!/usr/bin/env python3

import json
from sys import exit
from time import sleep
from pathlib import Path

import requests
import requests_cache
from dateutil import parser

from mongo import get_mongo
from models import get_version
from save import save

db = get_mongo()
models = get_version(1)

requests_cache.install_cache('replay_requests')


def main():
    delay = 0.5
    count = 3999
    url = "https://www.rocketleaguereplays.com/api/replays/?page=3999"
    r = requests.get(url)
    
    if not r.ok:
        exit(f"Initial request failed.\nResponse Code {r.status_code}")

    for f in r.json().get('results', []):
        if not parse(f):
            print("Failed to save result")

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
            if not parse(f):
                print("Failed to save result")

        next_url = r.json().get('next', False)
    
        
def parse(r: dict = {}):
    try:
        index = models.Index()
        index.pid = int(r['id'])
        index.replay_id = str(r['replay_id'])
        index.url = str(r['url'])
        index.file_url = str(r['file'])
        index.fps = int(r.get('record_fps', 30))
        if r.get('num_frames', False) and r.get('num_frames') != "null":
            index.num_frames = int(r.get('num_frames', 0))
        if r.get('map', False) and r.get('map') != "null":
            index.map_name = str(r['map']['title'])
        index.match_type = str(r.get('match_type', "Online"))
        index.season = int(r['season'].get("title", 5) \
                            .replace("Competitive Season ", "").replace("Season ", ""))
        index.excitement_factor = int(r.get('excitement_factor', 0))
        index.average_rating = int(r.get('average_rating', 0))
        if r.get('shot_data', False) and r.get('shot_data') != "null":
            index.shot_data = str(r.get('shot_data', ''))
        index.date_created =  parser.parse(str(r.get('date_created')))
        index.save()
        return True
    except Exception as e:
        # print(str(r))
        # print(e)
        return False


if __name__ == "__main__":
    main()
