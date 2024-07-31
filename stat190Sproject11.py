# Macie Wheeler
# Project 11

### Question 1

import pandas as pd

all_files = ["/class/datamine/data/fars/1975/ACCIDENT.CSV",
"/class/datamine/data/fars/1976/ACCIDENT.CSV",
"/class/datamine/data/fars/1977/ACCIDENT.CSV",
"/class/datamine/data/fars/1978/ACCIDENT.CSV", 
"/class/datamine/data/fars/1979/ACCIDENT.CSV",
"/class/datamine/data/fars/1980/ACCIDENT.CSV", 
"/class/datamine/data/fars/1981/ACCIDENT.CSV"]

file_list = []

for file in all_files:
  df = pd.read_csv(file)
  file_list.append(df)


accidents = pd.concat(file_list)
accidents["YEAR"] = "19" + accidents["YEAR"].astype(str)
accidents.head()

### Question 2

drunk_dr_and_sch_bus = accidents.loc[(accidents["DRUNK_DR"] >= 1) & (accidents["SCH_BUS"] == 1), :]
drunk_dr_and_sch_bus.shape[0]

# There are 101 accidents which involve 1 or more drunk drivers and a school bus.

### Question 3

drunk_dr_and_sch_bus.groupby("YEAR")["YEAR"].count()

# The year 1978 had the largest number of these types of accidents.

### Question 4

for i in range(0, 7):
  drunk_dr = accidents.loc[accidents["DRUNK_DR"] == i, :]
  mean_motorists = drunk_dr["PERSONS"].mean()
  print("The mean numbers of motorists involved in an accident with " +
  str(i) + " drunk drivers is: " + str(mean_motorists))


### Question 5

accidents.groupby(pd.cut(accidents["HOUR"], [0, 6, 12, 18, 24, 99], include_lowest = True))["FATALS"].sum()
accidents.groupby(pd.cut(accidents["HOUR"], [0, 6, 12, 18, 24, 99], include_lowest = True))["FATALS"].mean()
