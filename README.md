# Coronavirus twitter analysis

In this project I searched all geotagged tweets sent in 2020, monitoring for the spread of the coronavirus on twitter. I got practice:

1. working with large scale datasets
1. working with multilingual text
1. using the MapReduce divide-and-conquer paradigm to create parallel code

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
In total, there were about 1.1 billion tweets in this dataset.

The tweets in our class database, the lambda server, were stored as follows.
The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`,
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format.
JSON is a popular format for storing data that is closely related to python dictionaries.

## Procedure

I followed the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.

MapReduce is a famous procedure for large scale parallel processing that is widely used in industry. It is a 3 step procedure summarized in the following image:

<img src=mapreduce.png width=100% />

I modified the `map.py` file that tracked the usage of hashtags for both language and country. I created a shell script file `run_maps.sh` which looped over each file in the dataset and ran the `map.py` command on each file. This compiled in the `outputs` folder over the course of several hours. It was ran in parallel on the lambda server to increase speed. 

Once the `map.py` was finished running, I reduced the outputs into single files for language and country using `reduce.py`.


## Results

**Bar Graph Plots**
<img src=coronaviruscountry.png width=100% />
<img src=coronaviruslanguage.png width=100% />
<img src=코로나바이러스country.png width=100% />
<img src=코로나바이러스language.png width=100% />
For these plots I modified the `visualize.py` file so that it generated a bar graph of the results and stored them as a png file. The graphs above display the frequency of `#coronavirus` and `#코로나바이러스` for each country and language in the top 10 most frequent. 


**Line Graph Plot**
<img src=corona_covid19.png width=100% />
For this graph I created a new file `alternative_reduce.py`. This file  takes as input on the command line a list of hashtags, and outputs a line plot where comparing their frequency of use for each day in 2020. Above, I compared the frequency of two similar hashtags `#corona` and `#covid19`
