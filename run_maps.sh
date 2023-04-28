#!/bin/sh
for FILE in '/data/Twitter dataset/'geoTwitter20*; do
    ./src/map.py --input_path="$FILE" &
done
