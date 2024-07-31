# Macie Wheeler
# Project 9

### Question 1

import pandas as pd

beers = pd.read_parquet("/class/datamine/data/beer/beers.parquet")
breweries = pd.read_parquet("/class/datamine/data/beer/breweries.parquet")
reviews = pd.read_parquet("/class/datamine/data/beer/reviews.parquet")

def prepare_data(myDF: pd.DataFrame, min_num_reviews: int) -> pd.DataFrame:
  """
  This function accepts a data frame myDF and an integer min_num_reviews that
  represents the minimum amount of reviews that the user and the beer must have.
  
  Args:
    myDF (pd.DataFrame): a pandas data frame
    min_num_reviews (int): an integer representing the minimum amount of reviews
    the user and beer must have
  
  Returns:
    It will return a data frame such that all of the rows with score, username, or 
    beer_id missing will be removed and among the remaining rows the rows that will
    be kept are the ones that have a user (username) and a beer_id that each occur
    at least min_num_reviews times in myDF.
  """
  myDF = myDF.loc[myDF.loc[:, "score"].notna(), :]
  myDF = myDF.loc[myDF.loc[:, "username"].notna(), :]
  myDF = myDF.loc[myDF.loc[:, "beer_id"].notna(), :]
  myDF.reset_index(drop=True)
  
  goodusers = myDF.loc[:, "username"].value_counts() >= min_num_reviews
  goodusers = goodusers.loc[goodusers].index.values.tolist()
  
  goodbeerids = myDF.loc[:, "beer_id"].value_counts() >= min_num_reviews
  goodbeerids = goodbeerids.loc[goodbeerids].index.values.tolist()
  
  myDF = myDF.loc[myDF.loc[:, "username"].isin(goodusers) &
  myDF.loc[:, "beer_id"].isin(goodbeerids), :]
  
  return myDF
  

train = prepare_data(reviews, 1000)
print(train.shape) # (952105, 10)

### Question 2

def standardize(data: pd.DataFrame) -> pd.DataFrame:
  """
  This function takes in a dataframe and standardizes its score column.
  
  Args:
    data (pd.DataFrame): a pandas data frame
    
  Returns:
    A data frame with a new column of standardized scores.
  """
  data['mean'] = data['score'].mean()
  data['std'] = data['score'].std()
  
  data['standardized_score'] = (data['score'] - data['mean']) / data['std']
  return data
  

results = train.groupby(["username"]).apply(standardize)
results
  
### Question 3

score_matrix = results.pivot(index='username', columns='beer_id', values='standardized_score')
score_matrix

### Question 4

score_matrix.fillna(score_matrix.mean(axis=0))
