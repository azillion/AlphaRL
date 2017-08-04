#!/usr/bin/env python3
from time import sleep
from pathlib import Path

import fire
import grequests
# import requests

from mongo import get_mongo
from models import get_version

db = get_mongo()
models = get_version(1)


def save(r, **kwargs):
    try:
        if not r.ok:
            with open("failed.txt", "r+") as f:
                f.write(str(r.url))
            print(f"Replay {str(r.url)} failed to save.")

        replay = models.Index.objects(file_url=str(r.url)).first()

        path = Path("encoded").resolve()
        path = path / f"E{replay.replay_id}.replay"

        with open(path, 'wb') as file:
            file.write(r.content)

        replay.encoded_file_path = str(path.resolve())
        replay.downloaded = True
        replay.save()
        r.close()
        print(f"Replay {str(replay.pid)} saved to {str(path)}.")
    except Exception as e:
        print(e)


def async():
    count = 1
    x = 100
    replays = models.Index.objects(downloaded__ne=True)[:x]
    while len(replays) > 0:
        replay_urls = []

        if len(replays) < 100:
            x = len(replays)

        for i, replay in enumerate(replays):
            rs = grequests.get(replay.file_url, hooks=dict(response=save))
            replay_urls.append(rs)

        if (count % 50) == 0:
            print(f"Getting file set {str(count)}")

        grequests.map(replay_urls)

        count += 1
        replays = models.Index.objects(downloaded__ne=True)[:x]


if __name__ == '__main__':
    fire.Fire(async)
