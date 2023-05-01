#!/usr/bin/env python3

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
import matplotlib.pyplot as plt

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
plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)

if args.input_path[-1] == 'g':
    plt.xlabel('Language')
else:
    plt.xlabel('Country')
if args.percent:
    plt.ylabel('Percent of Total')
else:
    plt.ylabel('Amount of Tweets')

if args.input_path[-1] == 'g':
    plt.savefig(args.key[1:] + 'language.png')
    print(args.key[1:] + 'language.png')
else:
    plt.savefig(args.key[1:] + 'country.png')
    print(args.key[1:] + 'country.png')
