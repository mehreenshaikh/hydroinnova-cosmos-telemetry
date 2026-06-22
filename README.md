# Hydroinnova-Cosmos-Telemetry
Using the **SnowEx20 COSMOS Stationary Soil Moisture V001** dataset:
- source: _https://data.nasa.gov/dataset/snowex20-cosmos-stationary-soil-moisture-v001_
- user guide: _https://nsidc.org/sites/default/files/snex20_cssm-v001-userguide.pdf_

The data was stored in multiple file types recorded at different cadences.
Hydroinnova Cosmos Telemetry is a tool built with Python and PyCharm which combines all the data into a single set that can be plotted and analyzed. 

This was inspired by the LEIA Data Analysis and Test Support NASA internship posting. The LEIA protoflight unit integration and test campaign has generated a variety of datasets, including thermal, optical, power, and pressure. These data are stored in multiple file types recorded at different cadences. The project needs a tool that will combine all this data into a single set that can be plotted and analyzed. The created tool will support both ground testing and flight operations. Essentially, you would be working with a team to assemble a data analysis toolset to stitch data files together and allow users to extract, plot, and visualize outputs.

# Getting Started
1. Download the **nsidc-download_SNEX20_CSSM.001_2026-06-04.py** file and use it to download the rest of the files
2. Make sure libraries are installed (pandas as pd, Path from pathlib, plotly.express as px)
3. Run **telemetry.py**

# How I Did It
### 5/11/2026
1. I defined the logic of what I intended my project to do:
  	1. Import thermal, optical, power, pressure stored in multiple file types recorded at different cadences
    2. Put into one standard file type
    3. Allow for export
  	4. Stitch together datasets into a single set
  	5. Extract from datasets
  	6. Plot datasets
  	7. Visualize datasets
2. I began looking for training datasets on _NASA Open Data Portal_ and _Kaggle_ containing related probe data stored in different file types recorded at different cadences.
### 5/13/2026
2. I created a project in RStudio. I didn't end up continuing with R as I later switched to Python in PyCharm.
3. I identified the dataset I want to use as **SnowEx20 COSMOS Stationary Soil Moisture V001**, which contains temperature and pressure data.
### 5/18/2026
4. I found the dataset's home website and read through the user guide.
5. I tried downloading the dataset using EarthData but it was not downloading at all.
### 6/7/2026
6. I set up **main.py** (not included in this repository).
7. Instead of using EarthData, I used a given Python file (**nsidc-download_SNEX20_CSSM.001_2026-06-04.py**) to import the dataset's files.
### 6/8/2026
8. I specifically extracted 4 files (2 raw .txt and 2 .csv with corresponsing Dates).
9. I created a skeleton structure of comments about what the program would do in main.py (I later transferred this over to telemetry.py as well).
10. I cleaned the dataset by removing columns with inoperable and pretty unnecessary data.
### 6/10/2026
11. I fixed the timestamp columns by transferring it to Datetime class and standardizing their column names.
### 6/15/2026
12. I stitched together the datasets.
13. I started removing the NA value rows but I learnt that every row is missing a value in at least one of its columns (except for the timestamp column). If I removed NA rows, I would be emptying the entire dataframe, so I ommitted the NA-removing code instead.
14. I coded the program portion that allows for exporting the final dataset.
15. I started using streamlit library to build a user-interactive dashboard for plotting results.
### 6/16/2026
16. I finished the user-interactive plotting portion but I ran into an issue: streamlit doesn't always load and when it does, it takes FOREVER to do so.
### 6/20/2026
17. I tried debugging the streamlit method of user-interactive plotting but it still wasn't loading so I decided to switch from using streamlit (which opens a webpage where you can click which variable you want to plot) to plotly (you type in the terminal the column(s) you want to plot).
18. Based on **main.py**, I created telemetry.py which used the same algorithm but reads, cleans, stitches together, and plots ALL of **SnowEx20 COSMOS Stationary Soil Moisture V001**'s files.

# Moving Forward
Some ideas I have for future features and projects after completing Hydroinnova-Cosmos-Telemetry project are:
1. The user can choose to plot multiple values on the same plot or choose to do so on separate plots without having to rerun **telemetry.py**.
2. Splitting up the program into multiple files which can run sequentially and separately.
3. The user can choose the data visualization.
4. Making a full front-end portion for Hydroinnova-Cosmos-Telemetry.
5. A univeral data-cleaning program.
