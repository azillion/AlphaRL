#!/usr/bin/env python3
import subprocess
from time import sleep
from pathlib import Path
from multiprocessing import Pool

from mongo import get_mongo
from models import get_version

db = get_mongo()
models = get_version(1)


def convert(replay):
    try:
        if not replay:
            print("No file was provided")

        path = Path("encoded").resolve()
        path = path / f"E{replay.replay_id}.replay"
        
        new_path = Path("decoded").resolve()
        new_path = new_path / f"D{replay.replay_id}.json
        
        if path.exists() is False:
            return "Failed"
            
        subprocess.run(["rattletrap", str(path), str(new_path)])
        
        replay.parsed_file_path = str(new_path.resolve())
        replay.converted = True
        replay.save()
        
        print("Success")
    except CalledProcessError as e:
        print(e)
        return "Failed"


if __name__ == '__main__':
    count = models.Index.objects(converted__ne=True).count()
    while count > 0:
        unconverted = models.Index.objects(converted__ne=True)[:5000]
        with Pool() as p:
            print(p.map(convert, unconverted))
        count = models.Index.objects(converted__ne=True).count()
