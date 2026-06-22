import pandas as pd
from pathlib import Path
import plotly.express as px

DATA_DIR = Path(".")

#LOADING FUNCTIONS

def loadingL1txtFiles(data_dir):
    txt_files = list(data_dir.glob("SNEX20_CSSM_*_L1.txt")) #creates list
    dfs = []
    for file in txt_files:
        df = pd.read_csv(file, sep=",", skiprows = 21, engine="python")
        df["source_file"] = file.name
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def loadingL2csvFiles(data_dir):
    csv_files = list(data_dir.glob("SNEX20_CSSM_*_L2.csv")) #creates list
    dfs = []
    for file in csv_files:
        df = pd.read_csv(file)
        df["source_file"] = file.name
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

#LOAD ALL FILES

l1_data = loadingL1txtFiles(DATA_DIR) #5940 rows x 15 columns
l2_data = loadingL2csvFiles(DATA_DIR) #5938 rows x 5 columns

#CLEAN COLUMN NAMES

l1_data = l1_data.drop(columns=['T_CS215', 'RH_CS215', 'N1Cts', 'N2Cts', 'N1ET_sec', 'N2ET_sec', 'Unnamed: 13'], inplace=False) #5940 rows x 8 columns
    #drop inoperative temp and relative humidity sensors, tube 1 and 2 counts, and tube 1 and 2 times
    #cleantxt1 and cleantxt2 columns: 'RecordNum' | 'Date Time(UTC)' (yyyy/mm/dd hh:mm:00) | 'P4_mb' (atmospheric pressure in mbar from gauge 1) |
    #                 'P1_mb' (atmospheric pressure in mbar from gauge 2) | 'T1_C' (temp in Celsius from sensor 1) | 'RH1' (relative humidity from sensor 1),
    #                 'Vbat' (battery voltage)
l1_data.columns = l1_data.columns.str.strip() #removes extra whitespace if there is any
l2_data.columns = l2_data.columns.str.strip() #removes extra whitespace if there is any
l1_data["timestamp"] = pd.to_datetime(l1_data["Date Time(UTC)"], errors="coerce")
l2_data["timestamp"] = pd.to_datetime(
    l2_data["Date"].astype(str) + " " + l2_data["Time"].astype(str),
    errors="coerce"
)
l2_data.drop(columns=['Time (UTC)'], inplace=True)
l2_data.rename(columns={'Time': 'Time(UTC)'}, inplace= True)
    #creates timestamp in format yyyy/mm/dd hh:mm:ss for l2 files because l1 already has a timespace columns

#SORT DATA

l1_data = l1_data.sort_values("timestamp")
l2_data = l2_data.sort_values("timestamp")

#MERGE DATA

SNEX20 = pd.concat([l1_data, l2_data])
SNEX20 = SNEX20.sort_values("timestamp") #sort in ascending chronological order

print(SNEX20.isna().sum()) #checks for missing data and returns count of NaN in each column
                           #every column is missing values except source_file
#SNEX20.dropna(inplace=True) #remove rows with missing data
#print(SNEX20.isna().sum()) #checks again, should return 0 for all columns

#EXPORT DATA

while True:
    exportFile = input("Export data as a CSV? (Y/N): ").upper()
    if exportFile == "Y":
        SNEX20.to_csv('SNEX20.csv', index=False, na_rep='Unknown')
        print("File exported successfully.")
        break
        #future feature: export as Excel
    elif exportFile == "N":
        print("Export skipped.")
        break
    else:
        print("Please enter Y or N.")

print("Program continues below: ")

#PLOT DATA
plot_columns = ["P4_mb", "P1_mb", "T1_C", "RH1", "Vbat", "Cosmic-ray Soil Water Content (cm3/cm3)"]
print("Available columns:")
for i, col in enumerate(plot_columns):
    print(f"{i}: {col}")
choices = input("Choose column numbers separated by commas, example 0,2,3: ")
selected_cols = [
    plot_columns[int(i.strip())]
    for i in choices.split(",")
]
fig = px.line(
    SNEX20,
    x="timestamp",
    y=selected_cols,
    title="SNEX20 Telemetry Data"
)
fig.show()