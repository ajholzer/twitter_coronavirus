#!/usr/bin/env python3
import matplotlib.pyplot as plt

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

#plot
topten = items[:10]
keys, values = zip(*reversed(topten))

fig, ax = plt.subplots()
ax.barh(keys, values)
ax.set_xlabel('Number of Tweets')

if 'lang' in args.input_path:
    ax.set_ylabel('Language')
    fig.savefig(f'{args.key}_(lang).png')
else:
    ax.set_ylabel('Country')
    fig.savefig(f'{args.key}_(country).png')
