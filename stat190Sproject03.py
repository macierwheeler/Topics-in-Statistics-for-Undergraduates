# Macie Wheeler
# Project 3

### Question 1

import pandas as pd

myDF = pd.read_csv('/class/datamine/data/craigslist/vehicles.csv')
myDF.head()

### Question 2

years = myDF['year'].dropna().to_list()
unique_years = list(set(years))

my_dict = {}

for year in unique_years:
  my_dict[year] = 0
  
for y in years:
  my_dict[y] = my_dict[y] + 1
  
my_dict

### Question 3

my_dict[1912]

# One "key" from my_dict is 1912. This is the year that we are looking at.
# The associated value of that key is 5. This is the number of vehicles in our 
# dataset from the year 1912 on craigslist.

import matplotlib.pyplot as plt

keys = my_dict.keys()
values = my_dict.values()

plt.bar(keys, values)
plt.xlabel('Year')
plt.ylabel('Number of Cars From That Year')
plt.show()
plt.close()

### Question 4

listA = [1, 2, 3, 4, 5, 6, 12, 12]
listB = [2, 1, 7, 7, 7, 2, 8, 9, 10, 11, 12, 13]

setA = set(listA)
setB = set(listB)

# 1. values in list A but not list B
# values in list A but not list B
onlyA = setA.difference(setB)

print(onlyA) # [3, 4, 5, 6]

# 2. values in listB but not list A
onlyB = setB.difference(setA)

print(onlyB) # [7, 8, 9, 10, 11, 13]

# 3. values in both lists
# values in both lists
in_both_lists = setA.intersection(setB)

print(in_both_lists) # [1,2,12]

### Question 5

states_list = list(myDF.loc[:, ["state", "lat", "long"]].dropna().to_records(index=False))

geoDict = {}

for triple in states_list:
  geoDict[triple[0]] = []
  
for t in states_list:
  geoDict[t[0]].append((t[1], t[2]))


# don't have to run this part in rmd, but submit jpg
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame

usa = gpd.read_file('/class/datamine/data/craigslist/cb_2018_us_state_20m.shp')
usa.crs = {'init': 'epsg:4269'}

pts = [Point(y,x) for x, y in geoDict.get("tx")]
gdf = gpd.GeoDataFrame(geometry=pts, crs = 4269)
fig, gax = plt.subplots(1, figsize=(10,10))
base = usa[usa['NAME'].isin(['Hawaii', 'Alaska', 'Puerto Rico']) == False].plot(ax=gax, color='white', edgecolor='black')
gdf.plot(ax=base, color='darkred', marker="*", markersize=10)
plt.show()

# to save to jpg:
plt.savefig('q5.jpg')
plt.close()

### Question 6

prices_list = list(myDF.loc[:, ["year", "price"]].dropna().to_records(index=False))

price_dict = {}

for double in prices_list:
  price_dict[double[0]] = []

for d in prices_list:
  price_dict[d[0]].append(d[1])
  
key = 1950
values = price_dict[key]

plt.boxplot(values)
plt.show()
plt.close()



