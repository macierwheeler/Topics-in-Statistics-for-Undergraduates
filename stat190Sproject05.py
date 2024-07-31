# Macie Wheeler
# Project 5

### Question 1

from pathlib import Path

p_csv = Path('/class/datamine/data/stackoverflow/unprocessed/2018.csv')
size_in_bytes_csv = p_csv.stat().st_size
print(f'The 2018.csv file takes up {size_in_bytes_csv} bytes')

p_parquet = Path('/class/datamine/data/stackoverflow/unprocessed/2018.parquet')
size_in_bytes_parquet = p_parquet.stat().st_size
print(f'The 2018.parquet file takes up {size_in_bytes_parquet} bytes')

p_feather = Path('/class/datamine/data/stackoverflow/unprocessed/2018.feather')
size_in_bytes_feather = p_feather.stat().st_size
print(f'The 2018.feather file takes up {size_in_bytes_feather} bytes')

print(f'The parquet file is {(size_in_bytes_parquet / size_in_bytes_csv) * 100:.2f}% smaller than the csv file.')
print(f'The feather file is {(size_in_bytes_feather / size_in_bytes_csv) * 100:.2f}% smaller than the csv file.')

from block_timer.timer import Timer
import pandas as pd

with Timer(title="Reading in 2018.csv file") as t1:
  myDFcsv = pd.read_csv('/class/datamine/data/stackoverflow/unprocessed/2018.csv')

with Timer(title="Reading in 2018.parquet file") as t2:
  myDFparquet = pd.read_parquet('/class/datamine/data/stackoverflow/unprocessed/2018.parquet')
  
with Timer(title="Reading in 2018.feather file") as t3:
  myDFfeather = pd.read_feather('/class/datamine/data/stackoverflow/unprocessed/2018.feather')
  
print(f'Reading in the parquet file is {(t2.elapsed / t1.elapsed) * 100:.2f}% faster than reading in the csv file.')
print(f'Reading in the feather file is {(t3.elapsed / t1.elapsed) * 100:.2f}% faster than reading in the csv file.')

my2018 = pd.read_csv('/class/datamine/data/stackoverflow/unprocessed/2018.csv')

with Timer(title="Writing contents of my2018 to 2018.csv") as t4:
  my2018.to_csv('/scratch/scholar/wheele73/2018.csv')

with Timer(title="Writing contents of my2018 to 2018.parquet") as t5:
  my2018.to_parquet('/scratch/scholar/wheele73/2018.parquet')

with Timer(title="Writing contents of my2018 to 2018.feather") as t6:
  my2018.to_feather('/scratch/scholar/wheele73/2018.feather')

print(f'Writing the parquet file is {(t5.elapsed / t4.elapsed) * 100:.2f}% faster than writing the csv file.')
print(f'Writing the feather file is {(t6.elapsed / t4.elapsed) * 100:.2f}% faster than writing the csv file.')

### Question 2

notStudentPercent = sum(my2018['Student'] == 'No') / len(my2018['Student']) * 100
studentPercent = (1 - (notStudentPercent / 100)) * 100

notStudentPercent
studentPercent
# About 71.21% of the respondents are not students and about 28.79% of the respondents are students.

not_students = my2018.loc[my2018['Student'] == 'No', :]

### Question 3

profession_list = []

not_students['DevType'] = not_students['DevType'].astype(str)

for occupation in not_students.loc[:, 'DevType']:
  if (occupation != 'NaN'):
    list = occupation.split(';')
    for i in list:
      profession_list.append(i)

unique_professions = set(profession_list)
len(unique_professions)

# There are 22 unique professions.

not_students = not_students.loc[not_students['DevType'].str.contains('Student'), :]
not_students.shape

# There are 3723 respondents who replied 'No' to Student yet put 'Student' as one of the DevType's.

### Question 4

import random
import matplotlib.pyplot as plt

femaleDF = not_students.loc[not_students['Gender'] == 'Female', :]
femaleDF
femaleDF = femaleDF.reset_index()
f_age = []

for i in range(100):
  f_age.append(femaleDF.loc[random.randint(0, femaleDF.shape[0] - 1), "Age"])

series_f = pd.Series(f_age)
value_counts_f = series_f.value_counts()
value_counts_f

value_counts_f.plot.bar()
plt.title('Female Age Counts')
plt.show()
plt.close()

maleDF = not_students.loc[not_students['Gender'] == 'Male', :]
maleDF = maleDF.reset_index()
m_age = []

for i in range(100):
  m_age.append(maleDF.loc[random.randint(0, maleDF.shape[0] - 1), "Age"])

series_m = pd.Series(m_age)
value_counts_m = series_m.value_counts()
value_counts_m

value_counts_m.plot.bar()
plt.title('Male Age Counts')
plt.show()
plt.close()

### Question 5

fDF = my2018.loc[my2018['Gender'] == 'Female', :]
fDF = fDF.reset_index()

fmajors = fDF['UndergradMajor'].to_list()
series_fmajors = pd.Series(fmajors)
value_counts_fmajors = series_fmajors.value_counts()
value_counts_fmajors

value_counts_fmajors.plot.bar()
plt.title('Female Undergrad Major Distribution')
plt.show()
plt.close()

mDF = my2018.loc[my2018['Gender'] == 'Male', :]
mDF = mDF.reset_index()

mmajors = mDF['UndergradMajor'].to_list()
series_mmajors = pd.Series(mmajors)
value_counts_mmajors = series_mmajors.value_counts()
value_counts_mmajors

value_counts_mmajors.plot.bar()
plt.title('Male Undergrad Major Distribution')
plt.show()
plt.close()

# The most popular undergrad major among males and females in our 2018 dataframe is the same for both, 
# it being 'Computer science, computer engineering, or software engineering'.
# the least popular undergrad major among females is 'I never declared a major' and the least popular
# undergrad major among males is 'A health science (ex. nursing, pharmacy, radiology)'.
# The graphics above show the distribution of undergrad majors for both males and females.
