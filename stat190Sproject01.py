# Macie Wheeler
# Project 1

### Question 1
# The format options available to me are: Notebook (.ipynb), Python (.py),
# HTML (.html), Markdown (.md), reST (.rst), 
# LaTeX (.tex), and PDF via LaTeX (.pdf).

### Question 2
from thedatamine import hello_datamine
hello_datamine()

### Question 3
help(hello_datamine)
hello_datamine("Macie")

# The function hello_datamine said that it took one input, a string which is
# supposed to represent the name of the student. If there was no input then the
# function would default the name to 'student'. So, I modified the code from
# question 2 by adding a string of my name as an input for the function to make
# the message customized.

### Question 5

import csv

with open('/class/datamine/data/open_food_facts/openfoodfacts.tsv') as my_csv_file:
  my_reader = csv.reader(my_csv_file, delimiter = '\t')
  
  for row in my_reader:
    print(row)
    print(len(row))
    break
