import argparse
import json
import glob
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from collections import Counter, defaultdict

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

# Load data
data_by_date = defaultdict(lambda: Counter())
for file_path in glob.glob('outputs/geoTwitter*.lang'):
    with open(file_path) as f:
        data = json.load(f)
    date = file_path.split('.')[0][-8:]
    data_by_date[date].update(data)

# Compute tweet volume by date and key
volume_by_date_and_key = defaultdict(lambda: defaultdict(int))
for date, data in data_by_date.items():
    for key in args.keys:
        if key in data:
            volume_by_date_and_key[key][date] = sum(data[key].values())

# Plot data
fig, ax = plt.subplots()
for key, volume_by_date in volume_by_date_and_key.items():
    dates = sorted(volume_by_date.keys())
    values = [volume_by_date[date] for date in dates]
    days = [datetime.strptime(date, '%y-%m-%d') for date in dates]
    ax.plot(days, values, label=key[1:])

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))

# Add title and axis labels
ax.set_xlabel('Date')
ax.set_ylabel('Tweet Volume')
ax.legend()

# Save plot
tags = [key[1:] for key in args.keys]
filename = '_'.join(tags) + '.png'
plt.savefig(filename)
