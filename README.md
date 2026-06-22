# hydroinnova-cosmos-telemetry
Using the **SnowEx20 COSMOS Stationary Soil Moisture V001** dataset:
- source: _https://data.nasa.gov/dataset/snowex20-cosmos-stationary-soil-moisture-v001_
- user guide: _https://nsidc.org/sites/default/files/snex20_cssm-v001-userguide.pdf_
The data was stored in multiple file types recorded at different cadences.
Hydroinnova Cosmos Telemetry is a tool built with Python and PyCharm which combines all the data into a single set that can be plotted and analyzed. 

This was inspired by the LEIA Data Analysis and Test Support NASA internship posting with the following description:
Work with the Lunar Explorer Instrument for space biology Applications (LEIA) team to assemble a data analysis toolset to stitch data files together and allow users to extract, plot, and visualize outputs. The LEIA protoflight unit integration and test campaign has generated a variety of datasets, including thermal, optical, power, and pressure. These data are stored in multiple file types recorded at different cadences. The project needs a tool that will combine all this data into a single set that can be plotted and analyzed. The created tool will support both ground testing and flight operations.
There will also be opportunities to support flight hardware assembly and testing in the lab. As well as to use the data tool to analyze test data in support of requirements verification and project milestone review materials.
Multiple weekly meetings with project team as well as mentor(s). Internship can be either full or part-time.
Computer programming skills in a suitable data analysis language such as Python or R preferred, but alternate languages are acceptable. Some familiarity with statistics and data analysis would be helpful. Ability to work independently coupled with inclination to ask questions.

# getting started
1. Download the **nsidc-download_SNEX20_CSSM.001_2026-06-04.py** file and use it to download the rest of the files
2. Make sure libraries are installed (pandas as pd, Path from pathlib, plotly.express as px)
3. Run **telemetry.py**
