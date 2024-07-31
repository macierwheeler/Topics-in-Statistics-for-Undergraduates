# Macie Wheeler
# Project 8

### Question 1

import pandas as pd

users = pd.read_parquet("/class/datamine/data/yelp/data/parquet/users.parquet")

def get_friends_data(user_id: str) -> pd.DataFrame:
  """
  This function accepts a string user id as an argument, and returns a pandas
  DataFrame with the information in the users DataFrame for each friend of the 
  user id.
  
  Args:
    user_id (str): a user id in string form
    
  Returns:
    pd.DataFrame: a pandas dataframe that has all of the information from the 
    users DataFrame for each friend of user_id
  """
  
  myDF = pd.DataFrame()
  for i in range(0, users.shape[0]):
    if users['user_id'][i] == user_id:
      friends_list = users['friends'][i]
      for j in range(0, users.shape[0]):
        if users['user_id'][j] in friends_list:
          myDF = myDF.append(users.iloc[j])
  return myDF

print(get_friends_data("ntlvfPzc8eglqvk92iDIAw").shape) # (13,22)
print(get_friends_data("AY-laIws3S7YXNl_f_D6rQ").shape) # (1, 22)
print(get_friends_data("xvu8G900tezTzbbfqmTKvA").shape) # (193,22)

### Question 2

reviews = pd.read_parquet("/class/datamine/data/yelp/data/parquet/reviews.parquet")

def calculate_avg_business_stars(business_id: str) -> float:
  """
  This function accepts a string business id as an argument, and returns the
  average number of stars that the given business received in reviews.
  
  Args:
    business_id (str): a business id in string form
    
  Returns:
    an float of the average number of stars that the given business received
    in reviews
  """
  
  count = 0
  review_stars = 0
  for i in range(0, reviews.shape[0]):
    if reviews['business_id'][i] == business_id:
      count = count + 1
      review_stars = review_stars + reviews['stars'][i]

  return review_stars / count
  
print(calculate_avg_business_stars("f9NumwFMBDn751xgFiRbNA")) # 3.1025641025641026

### Question 3

import matplotlib.pyplot as plt

def visualize_stars_over_time(business_id: str):
  """
  This function accepts a string business id as input, and returns a line plot
  that shows the average number of stars for each year the business has review data.
  
  Args:
    business_id (str): a business id in string form
    
  Returns:
    a line plot that show the average number of stars for each year the given 
    business has review data
  """
  
  myyears = []
  for i in range(0, reviews.shape[0]):
    myyears.append(reviews['date'][i].year)
  reviews['year'] = myyears
  
  averagestars = reviews.groupby(['business_id', 'year'], as_index = False)['stars'].mean()
  
  mydict = {}
  for i in range(0, averagestars.shape[0]):
    if averagestars['business_id'][i] == business_id:
      mydict[averagestars['year'][i]] = averagestars['stars'][i]
      
  plt.plot(mydict.keys(), mydict.values())
  plt.xlabel('Years')
  plt.ylabel('Average number of stars')
  plt.show()
  plt.close()

visualize_stars_over_time('RESDUcs7fIiihp38-d6_6g')

### Question 4

def visualize_stars_over_time(business_id: str, granularity: str = "years"):
  """
  This function accepts a string business id and a string granularity as input,
  and returns a line plot that shows the average number of stars for each year
  or for each month the business has review data.
  
  Args:
    business_id (str): a business id in string form
    granularity (str): a string of whether or not months or years should be graphed
    
  Returns:
    a line plot that show the average number of stars for each year or month the given 
    business has review data
  """
  
  myyearsormonths = []
  if granularity == "months":
    for i in range(0, reviews.shape[0]):
      myyearsormonths.append(reviews['date'][i].month)
  else:
    for i in range(0, reviews.shape[0]):
      myyearsormonths.append(reviews['date'][i].year)
  reviews['yearormonth'] = myyearsormonths
  
  averagestars = reviews.groupby(['business_id', 'yearormonth'], as_index = False)['stars'].mean()
  
  mydict = {}
  for i in range(0, averagestars.shape[0]):
    if averagestars['business_id'][i] == business_id:
      mydict[averagestars['yearormonth'][i]] = averagestars['stars'][i]
      
  plt.plot(mydict.keys(), mydict.values())
  if granularity == "months":
    plt.xlabel('Months')
  else:
    plt.xlabel('Years')
  plt.ylabel('Average number of stars')
  plt.show()
  plt.close()

visualize_stars_over_time('RESDUcs7fIiihp38-d6_6g', "months")

### Question 5

def visualize_stars_over_time(*args, **kwargs):
  """
  This function accepts a string business id, that can have multiple business ids
  and a string granularity as input,
  and returns a line plot that shows the average number of stars for each year
  or for each month the business has review data.
  
  Args:
    business_id (str): a business id in string form, can be multiple
    granularity (str): a string of whether or not months or years should be graphed
    
  Returns:
    a line plot that show the average number of stars for each year or month the given 
    business or businesses have review data
  """
  
  granularity = ""
  businesses = []
  
  if len(kwargs) > 0:
    granularity = kwargs['granularity']
    businesses = args
  else:
    granularity = args[len(args) - 1]
    businesses = args[0:len(args) - 1]
  
  for business_id in businesses:
    myyearsormonths = []
    if granularity == "months":
      for i in range(0, reviews.shape[0]):
        myyearsormonths.append(reviews['date'][i].month)
    else:
      for i in range(0, reviews.shape[0]):
        myyearsormonths.append(reviews['date'][i].year)
    reviews['yearormonth'] = myyearsormonths
  
    averagestars = reviews.groupby(['business_id', 'yearormonth'], as_index = False)['stars'].mean()
  
    mydict = {}
    for i in range(0, averagestars.shape[0]):
      if averagestars['business_id'][i] == business_id:
        mydict[averagestars['yearormonth'][i]] = averagestars['stars'][i]
      
    plt.plot(mydict.keys(), mydict.values())
    if granularity == "months":
      plt.xlabel('Months')
    else:
      plt.xlabel('Years')
    plt.ylabel('Average number of stars')
    plt.show()
    plt.close()

visualize_stars_over_time("RESDUcs7fIiihp38-d6_6g", "4JNXUYY8wbaaDmk3BPzlWw", "months")
visualize_stars_over_time("RESDUcs7fIiihp38-d6_6g", "4JNXUYY8wbaaDmk3BPzlWw", "K7lWdNUhCbcnEvI0NhGewg", "months")
visualize_stars_over_time("RESDUcs7fIiihp38-d6_6g", "4JNXUYY8wbaaDmk3BPzlWw", "K7lWdNUhCbcnEvI0NhGewg", granularity="years")

### Question 6

def visualize_stars_over_time(*args, **kwargs):
  """
  This function accepts a string business id, that can have multiple business ids
  and a string granularity as input,
  and returns a line plot that shows the average number of stars for each year
  or for each month the business has review data.
  
  Args:
    business_id (str): a business id in string form, can be multiple
    granularity (str): a string of whether or not months or years should be graphed
    
  Returns:
    a line plot that show the average number of stars for each year or month the given 
    business or businesses have review data
  """
  
  granularity = ""
  businesses = []
  
  if len(kwargs) > 0:
    granularity = kwargs['granularity']
    businesses = args
  else:
    granularity = args[len(args) - 1]
    businesses = args[0:len(args) - 1]
  
  for business_id in businesses:
    myyearsormonths = []
    if granularity == "months":
      for i in range(0, reviews.shape[0]):
        myyearsormonths.append(reviews['date'][i].month)
    else:
      for i in range(0, reviews.shape[0]):
        myyearsormonths.append(reviews['date'][i].year)
    reviews['yearormonth'] = myyearsormonths
  
    averagestars = reviews.groupby(['business_id', 'yearormonth'], as_index = False)['stars'].mean()
  
    mydict = {}
    for i in range(0, averagestars.shape[0]):
      if averagestars['business_id'][i] == business_id:
        mydict[averagestars['yearormonth'][i]] = averagestars['stars'][i]
      
    plt.plot(mydict.keys(), mydict.values())
    if granularity == "months":
      plt.xlabel('Months')
    else:
      plt.xlabel('Years')
    plt.ylabel('Average number of stars')
    plt.show()
    plt.close()

our_businesses = ["RESDUcs7fIiihp38-d6_6g", "4JNXUYY8wbaaDmk3BPzlWw", "K7lWdNUhCbcnEvI0NhGewg"]

# modify something below to make this work:
visualize_stars_over_time(*our_businesses, granularity="years")
