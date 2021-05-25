# Get 10000 random numbers (0 - 69999)
# Get corresponding google image
# use generator in order to generate 10k random numbers
# use generator to load up json file ?

import json
import random
import pprint
from datetime import datetime as dt

FILE_PATH = "ffhq-dataset-v2.json"
NO_OF_SAMPLES = 5

randomNos = random.sample(range(70000), NO_OF_SAMPLES)

timeA = dt.now()

res = []

d = dict()
with open(FILE_PATH, 'r') as f:
    data = json.loads(f.read())

    for i in randomNos:
        data[str(i)]['image']['id'] = i
        res.append(data[str(i)]['image'])
        d[i] = res[-1]


for k, v in d.items():
    print(k, v, '\n\n')

with open("out.json", "w") as f:
    json.dump(res, f)

timeB = dt.now()

print('Time to extract from json file = ' + str(timeB - timeA))