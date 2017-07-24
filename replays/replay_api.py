 #!/usr/bin/env python3

import json
from sys import exit
from time import sleep
from pathlib import Path

import requests

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

def main():
    delay = 0.5
    url = "https://www.rocketleaguereplays.com/api/replays/"
    r = requests.get(url)
    
    if not r.ok:
        exit(f"Initial request failed.\nResponse Code {r.status_code}")

    for f in r.json().get('results', []):
        file_url = f.get('file', None)
        f_r = save(file_url)
        if f_r is False:
            print(f"Failed to retrieve {file_url}")

    next_url = r.json().get('next', False)
    while next_url is not False:
        r = requests.get(next_url)
        while not r.ok:
            if delay > 1800:
                exit("Throttled too hard")
            sleep(delay)
            delay *= 1.5
            r = requests.get(next_url)

        for f in r.json().get('results', []):
            file_url = f.get('file', None)
            f_r = save(file_url)
            if f_r is False:
                print(f"Failed to retrieve {file_url}")

        next_url = r.json().get('next', False)


if __name__ == "__main__":
    main()