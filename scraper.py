import sys
import json

from parser import VideoParser

if '__main__': 

    res = {}

    with open('input.json') as input:
        liste_id = json.load(input)

    for id in liste_id['videos_id']:
        data = VideoParser(id).get_dict()
        res[id] = data

    with open("output.json", "w") as fp:
        json.dump(res, fp)
    j = json.dumps(res)
