# hydroinnova-cosmos-telemetry
Using the **SnowEx20 COSMOS Stationary Soil Moisture V001** dataset:
- source: _https://data.nasa.gov/dataset/snowex20-cosmos-stationary-soil-moisture-v001_
- user guide: _https://nsidc.org/sites/default/files/snex20_cssm-v001-userguide.pdf_
The data was stored in multiple file types recorded at different cadences.
Hydroinnova Cosmos Telemetry is a tool built with Python and PyCharm which combines all the data into a single set that can be plotted and analyzed. 

This was inspired by the LEIA Data Analysis and Test Support NASA internship posting. The LEIA protoflight unit integration and test campaign has generated a variety of datasets, including thermal, optical, power, and pressure. These data are stored in multiple file types recorded at different cadences. The project needs a tool that will combine all this data into a single set that can be plotted and analyzed. The created tool will support both ground testing and flight operations. Essentially, you would be working with a team to assemble a data analysis toolset to stitch data files together and allow users to extract, plot, and visualize outputs.

# getting started
1. Download the **nsidc-download_SNEX20_CSSM.001_2026-06-04.py** file and use it to download the rest of the files
2. Make sure libraries are installed (pandas as pd, Path from pathlib, plotly.express as px)
3. Run **telemetry.py**
