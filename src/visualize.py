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
import pandas as pd

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
frequency = []
hashtag = []

for k,v in items:
    hashtag.append(k)
    frequency.append(v)
df = pd.DataFrame(
        {'Hashtag': hashtag,
            'Frequency': frequency}
        )

df = df.sort_values('Frequency', ascending=True).tail(10)
df.plot(kind='bar', x='Hashtag', y='Frequency', legend=False)
plt.xlabel('')
plt.ylabel('')
plt.savefig(f"{args.key}country.png")
