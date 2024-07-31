## Macie Wheeler
## Project 2

### Question 1

import pandas as pd
from pathlib import Path

myDF = pd.read_csv('/class/datamine/data/craigslist/vehicles.csv')

p = Path('/class/datamine/data/craigslist/vehicles.csv')
print(f'Size in bytes: {p.stat().st_size}')
print(f'Size in Gigabytes: {p.stat().st_size/1_000_000_000}')

### Question 2

print(f'There are {myDF.shape[1]} columns in the DataFrame!')
print(f'There are {myDF.shape[0]} rows in the DataFrame!')

### Question 3

our_columns = list(myDF.columns)
our_columns
our_columns.append("extra")
our_columns
our_columns[1]
our_columns[0:len(our_columns):2]
our_columns[-4:]
our_columns.remove("extra")
our_columns

### Question 4

import matplotlib.pyplot as plt

my_values = tuple(myDF.loc[:, 'odometer'].dropna().to_list())

my_values = list(my_values)
my_values.sort()

plt.plot(my_values[0:-50])
plt.xlabel("Car Number")
plt.ylabel("Odometer Reading")
plt.show()
plt.close()

### Question 5

newest_car = myDF.iloc[myDF[['year']].idxmax()]
oldest_car = myDF.iloc[myDF[['year']].idxmin()]

newest_car[['model', 'year', 'price']]
oldest_car[['model', 'year', 'price']]

# The oldest car in this data set is a 1900 flatbed that has a price of $900.
# The newest car in this data set is a 2021 Honda-Nissan-Kia-Ford-Hyndai-VW and 
# it doesn't currently have a price on it.
