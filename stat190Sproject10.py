# Macie Wheeler
# Project 10

### Question 1

import pandas as pd
import numpy as np

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

score_matrix = results.pivot(index='username', columns='beer_id', values='standardized_score')

score_matrix = score_matrix.fillna(score_matrix.mean(axis=0))

from sklearn.metrics.pairwise import cosine_similarity

cosine_similarity_array = cosine_similarity(score_matrix)
np.fill_diagonal(cosine_similarity_array, 0)

cosine_similarity_matrix = pd.DataFrame(cosine_similarity_array)
cosine_similarity_matrix.index = score_matrix.index
cosine_similarity_matrix.columns = score_matrix.index

cosine_similarity_matrix.head()

### Question 2

def get_knn(cosine_similarity_matrix: pd.DataFrame, username: str, k: int) -> list:
  """
  This function takes in a cosine similarity matrix, a username, and a k value
  and returns a list containing the usernames of the k most similar users
  to the input username.
  
  Args:
    cosine_similarity_matrix (pd.DataFrame): a pandas data frame
    username (str): a username in string form
    k (int): a number k
  
  Returns:
    A list contianing the usernames of the k most similar users
    to the input username.
  """
  
  result = cosine_similarity_matrix[username].sort_values(ascending=False)[0:k].index.tolist()
  
  return result
  

k_similar=get_knn(cosine_similarity_matrix,"2GOOFY",4)
print(k_similar) # ['Phil-Fresh', 'mishi_d', 'SlightlyGrey', 'MI_beerdrinker']

### Question 3

user = 'zotzot'
most_similar_other_user = get_knn(cosine_similarity_matrix, user, 1)
other_user = most_similar_other_user[0]

user_list = []
user_list.append(user)
user_list.append(other_user)

aux = reviews[reviews["username"].isin(user_list)]
aux = pd.pivot_table(aux, values='score', index='beer_id', columns='username')
aux = aux.dropna(axis=0, how='any')
aux = aux.sort_values(by=user_list[0])
aux

# It looks as if the users rated the beers similarly. Most of the differences
# between the two users' scores are within about .5 of each other. There are
# only a handful of times where there is a difference of 1 between the two
# users' scores.

### Question 4

def recommend_beers(train: pd.DataFrame, myusername: str, cosine_similarity_matrix: pd.DataFrame, k: int):
  """
  This function take in a train data frame, a username, a cosine similarity matrix,
  and a k value (how many neighbors to use) and returns the top 5 beer recommendations
  for the user.
  
  Args:
    train (pd.DataFrame): a pandas data frame 
    myusername (str): a username in string form
    cosine_similarity_matrix (pd.DataFrame): a pandas data frame
    k (int): a number k which represents how many neighbors to use
    
  Returns:
    The top 5 beer recommendations for the user
  """
  
  neighbors = get_knn(cosine_similarity_matrix, myusername, k)
  
  aux = train.loc[train.loc[:, "username"].isin(neighbors)]
  tempDF = train.loc[train.loc[:, "username"].isin([myusername])]
  beer_id_list = tempDF['beer_id'].tolist()
  
  beers_not_reviewed_by_user = aux.loc[aux.loc[:, "beer_id"].isin(beer_id_list) == False]
  
  beers_not_reviewed_by_user = standardize(beers_not_reviewed_by_user)
  grouped = beers_not_reviewed_by_user.loc[:, ("beer_id", "standardized_score")].groupby(["beer_id"]).mean()
  results = grouped.sort_values(by='standardized_score', ascending=False).index.tolist()
  return results[0:5]


recommend_beers(train, "22Blue", cosine_similarity_matrix, 30) # [40057, 69522, 22172, 59672, 86487]
