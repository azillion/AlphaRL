#!/usr/bin/env python3

import json

from redis_f import formatter

def main():
    data = {}
    with open("output2.json") as f:
        data = json.load(f)
    
    k_set = list(map(lambda k: "f" + str(k), range(len(data['content']['frames']))))
    
    with open('redis.txt', 'w') as f:
        h_count = 0
        frames = data['content']['frames']
        while len(frames) > 0:
            temp_frames = []
            if len(frames) >= 100:
                list(map(lambda i: 
                    temp_frames.append(
                        {
                            str(k_set.pop(0)): json.dumps(
                                frames.pop(0), \
                                separators=(',', ':'))
                        }
                        ), range(100)))
            else:
                list(map(lambda i: 
                    temp_frames.append(
                        {
                            str(k_set.pop(0)): json.dumps(
                                frames.pop(0), \
                                separators=(',', ':'))
                        }
                        ), range(len(frames))))
                        
            h = "h" + str(h_count)
            f.write(formatter('hmset', h, temp_frames))
        return

if __name__ == "__main__":
    main()
