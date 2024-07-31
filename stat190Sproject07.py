# Macie Wheeler
# Project 7

### Question 1

from pathlib import Path
import pandas as pd

path1 = Path('/class/datamine/data/yelp/data/parquet/businesses.parquet')
size_in_bytes_1 = path1.stat().st_size
print(f'The business.parquet file takes up {size_in_bytes_1} bytes')
df1 = pd.read_parquet('/class/datamine/data/yelp/data/parquet/businesses.parquet')
df1[0:5]
df1.columns
# The first dataset is called businesses. It seems to show things like a
# businesses id, name and address, location, rating, and hours.

path2 = Path('/class/datamine/data/yelp/data/parquet/checkins.parquet')
size_in_bytes_2 = path2.stat().st_size
print(f'The checkins.parquet file takes up {size_in_bytes_2} bytes')
df2 = pd.read_parquet('/class/datamine/data/yelp/data/parquet/checkins.parquet')
df2[0:5]
df2.columns
# This second dataset is called checkins. It seems to show the business id
# and the date that someone checked into that business.

path3 = Path('/class/datamine/data/yelp/data/parquet/photos.parquet')
size_in_bytes_3 = path3.stat().st_size
print(f'The photos.parquet file takes up {size_in_bytes_3} bytes')
df3 = pd.read_parquet('/class/datamine/data/yelp/data/parquet/photos.parquet')
df3[0:5]
df3.columns
# This third dataset is called photos. It seems to show the photo id, business id,
# and caption and label for a photo that a business has.

path4 = Path('/class/datamine/data/yelp/data/parquet/reviews.parquet')
size_in_bytes_4 = path4.stat().st_size
print(f'The reviews.parquet file takes up {size_in_bytes_4} bytes')
df4 = pd.read_parquet('/class/datamine/data/yelp/data/parquet/reviews.parquet')
df4[0:5]
df4.columns
# This fourth dataset is called reviews. It seems to show things relating to reviews
# that users gave, it includes columns like the review id, business id, user id,
# and the text and date of the review.

path5 = Path('/class/datamine/data/yelp/data/parquet/tips.parquet')
size_in_bytes_5 = path5.stat().st_size
print(f'The tips.parquet file takes up {size_in_bytes_5} bytes')
df5 = pd.read_parquet('/class/datamine/data/yelp/data/parquet/tips.parquet')
df5[0:5]
df5.columns
# This fifth dataset is called tips. It seems to have things such as the user id,
# business id, some text that is most likely a tip, a date, and a compliment count.

path6 = Path('/class/datamine/data/yelp/data/parquet/users.parquet')
size_in_bytes_6 = path6.stat().st_size
print(f'The users.parquet file takes up {size_in_bytes_6} bytes')
df6 = pd.read_parquet('/class/datamine/data/yelp/data/parquet/users.parquet')
df6[0:5]
df6.columns
# This sixth dataset is called users. It seems to have things such as the user id,
# the user's name, the number of reviews they've made, their average stars, and
# things relating to the compliments.

### Question 2

businesses = pd.read_parquet('/class/datamine/data/yelp/data/parquet/businesses.parquet')
businesses['hours']
businesses['attributes']

def has_attributes(business_id):
  return_value = False
  for i in range(0, businesses.shape[0]):
    if (businesses['business_id'][i] == business_id):
      if (businesses['attributes'][i] != None):
        return True
  return return_value
  
print(has_attributes('f9NumwFMBDn751xgFiRbNA')) # True
print(has_attributes('XNoUzKckATkOD1hP6vghZg')) # False
print(has_attributes('Yzvjg0SayhoZgCljUJRF9Q')) # True
print(has_attributes('7uYJJpwORUbCirC1mz8n9Q')) # False

### Question 3

type(businesses.loc[:, "attributes"].iloc[0])

# The type of the value is a dictionary.

def fix_businesses_data(data_path: str, output_dir: str) -> None:
    """
    fix_data accepts a parquet file that contains data in a specific format. 
    fix_data "explodes" the attributes and hours columns into 39+7=46 new 
    columns.
    Args:
        data_path (str): Full path to a file in the same format as businesses.parquet.
        output_dir (str): Path to a directory where new_businesses.parquet should be output.
    """
    # read in original parquet file
    businesses = pd.read_parquet(data_path)
    
    # unnest the attributes column
    attributes_df = businesses.loc[:, "attributes"].apply(pd.Series)
    
    # unnest the hours column
    hours_df = businesses.loc[:, "hours"].apply(pd.Series)
    
    myDF = pd.concat([attributes_df, hours_df], axis=1)
    
    # output new file
    myDF.to_parquet(str(Path(f"{output_dir}").joinpath("new_businesses.parquet")))
    
    return None

my_username = "wheele73"
fix_businesses_data(data_path="/class/datamine/data/yelp/data/parquet/businesses.parquet", output_dir=f"/scratch/scholar/{my_username}")

# see if output exists
p = Path(f"/scratch/scholar/{my_username}").glob('**/*')
files = [x for x in p if x.is_file()]
print(files)

### Question 4

def unnest(myDF: pd.DataFrame, columns: list) -> pd.DataFrame:
  df = pd.DataFrame()
  for column in columns:
    tempDF = myDF.loc[:, column].apply(pd.Series)
    df = pd.concat([df, tempDF], axis = 1)
  return df

businesses = pd.read_parquet("/class/datamine/data/yelp/data/parquet/businesses.parquet")

new_businesses_df = unnest(businesses, ["attributes", ])
new_businesses_df.shape # (209393, 39)
new_businesses_df.head()

new_businesses_df = unnest(businesses, ["attributes", "hours"])
new_businesses_df.shape # (209393, 46)
new_businesses_df.head()

### Question 5

def unnest(myDF: pd.DataFrame, columns: list) -> pd.DataFrame:
  df = pd.DataFrame()
  for column in columns:
    if (column in myDF.columns):
      mySum = 0
      for i in range(0, myDF.shape[0]):
        if (isinstance(myDF[column][i], dict)):
          mySum = mySum + 1
      if (mySum > 0):
        tempDF = myDF.loc[:, column].apply(pd.Series)
        df = pd.concat([df, tempDF], axis = 1)
  return df

businesses = pd.read_parquet("/class/datamine/data/yelp/data/parquet/businesses.parquet")

results = unnest(businesses, ["doesntexist", "postal_code", "attributes"])
results.shape # (209393, 39)
results.head()

