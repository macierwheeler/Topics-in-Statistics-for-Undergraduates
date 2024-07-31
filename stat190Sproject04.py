# Macie Wheeler
# Project 4

### Question 1

import pandas as pd

myDF = pd.read_csv('/class/datamine/data/craigslist/vehicles.csv')

geoDict = {}
newDF = pd.DataFrame(columns = ['state', 'lat', 'long'])

for i in range(0, 20000):
  newDF = newDF.append({'state' : myDF['state'][i], 'lat' : myDF['lat'][i], 'long' : myDF['long'][i]}, ignore_index = True)

for index, row in newDF.iterrows():
  geoDict[row['state']] = []

for i, r in newDF.iterrows():
  geoDict[r['state']].append((r['lat'], r['long']))
  
### Question 2

states_list = list(myDF.loc[:, ["state", "lat", "long"]].dropna().to_records(index=False))

geoDict = {}
for mytriple in states_list:
  geoDict[mytriple[0]] = []
for mytriple in states_list:
  geoDict[mytriple[0]].append( (mytriple[1],mytriple[2]) )

for state in geoDict.keys():
  print(f'{state}:')
  for index, pair in enumerate(geoDict[state]):
    if (index % 5000 == 0):
      print(f'Lat: {pair[0]:.2f}, Long: {pair[1]:.2f}')

### Question 3

import os
import sys
import matplotlib.pyplot as plt
 
def partition(arr, low, high):
  end = high
  key = arr[high]
  while low < high:
    while low < high and arr[low] < key:
      low = low + 1
    while low < high and arr[high] >= key:
      high = high - 1
    if low < high:
      arr[low], arr[high] = arr[high], arr[low]
    arr[high], arr[end] = arr[end], arr[high]
  return high

def getMid(arr):
  pos = 0
  if (len(arr) > 1):
    start = 0
    end = len(arr) - 1
    if len(arr) % 2 == 1:
      mid = len(arr)/2
    else:
      mid = len(arr)/2 - 1
    while start < end:
      pos = partition(arr, start, end)
      if pos == mid:
        break
      elif pos > mid:
        end = pos - 1 
      else:
        start = pos + 1
  return arr[pos]

my_list = list(myDF.loc[:, ["year", "price",]].dropna().to_records(index=False))

year_dict = {}

for year in my_list:
  year_dict[year[0]] = []
for y in my_list:
  year_dict[y[0]].append(y[1])

median_car_price = {}

for year in year_dict.keys():
  median_car_price[year] = getMid(year_dict[year])

plt.bar(median_car_price.keys(), median_car_price.values())
plt.show()
plt.close()

### Question 4

import statistics

mean_car_price = {}

for year in year_dict.keys():
  if (statistics.mean(year_dict[year]) < 999999):
    mean_car_price[year] = statistics.mean(year_dict[year])

plt.bar(mean_car_price.keys(), mean_car_price.values())
plt.show()
plt.close()

### Question 5

my_list = list(myDF.loc[:, ["state", "price",]].dropna().to_records(index=False))

indiana_list = [price for (state, price) in my_list if state == 'in']
sum(indiana_list) / len(indiana_list)

combined_state_list = [price for (state, price) in my_list if state == 'in' or state == 'mi' or state == 'il']
sum(combined_state_list) / len(combined_state_list)

my_list = list(myDF.loc[:, ["manufacturer", "year", "price",]].dropna().to_records(index=False))

honda_list = [price for (manufacturer, year, price) in my_list if manufacturer == 'honda' and year >= 2010]
sum(honda_list) / len(honda_list)

### Question 6

import spacy
import re

# get list of descriptions
my_list = list(myDF.loc[:, ["description",]].dropna().to_records(index=False))
my_list = [m[0] for m in my_list]

# load the pre-built spacy model
nlp = spacy.load("en_core_web_lg")

# apply the model to a description
doc = nlp(my_list[0])

# print the text and label of each "entity"
for entity in doc.ents:
    print(entity.text.encode('ascii', errors='ignore'), entity.label_)

# The label of the majority of the phone numbers I can see is CARDINAL.

for i in range(0, 100):
  doc = nlp(my_list[i])
  for entity in doc.ents:
    if (entity.label_ == 'CARDINAL'):
      if (len(entity.text.encode('ascii', errors='ignore')) in (7, 8, 10, 11, 12, 14)):
        if (bool(re.search('[a-zA-Z]', entity.text.encode('ascii', errors='ignore').decode("utf-8"))) == False):
          print(entity.text.encode('ascii', errors='ignore'), entity.label_)

# My new filter in the for loop checks to see if there are any letters in the entity.
# If there aren't then it will print out that entity, which should now look more like
# a phone number.


