# Macie Rose Wheeler
# Project 1

### Question 1

#  The memory of the 7 frontend nodes is: 4 * 512 + 3 * 768 = 4352 GB.
#  The number of cores for the 7 frontend nodes is: 7 * 20 = 140 cores.

#  The memory of the 28 sub-clusters nodes is: 24 * 64 + 4 * 192 = 2304 GB.
#  The number of cores for the 28 sub-clusters is: 24 * 20 + 4 * 16 = 544 cores.

#  My personal computer has 8 GB of memory.
#  My personal computer has 4 cores.

### Question 2

#  (Type control-return to run a line of R code)

#  The node we are working on is:
system("hostname")

#  I am working on Scholar front end number 0.

### Question 3

#  The welcome message is:
#  "You've successfully loaded the Data Mine R settings!"

### Question 4

#  There are 3 chunks of R code, 1 chunk of bash, 1 chunk of Python, and 1 chunk of SQL.

### Question 5

#  We store 1, 2, 3 into the variable my_variable, and then we display output: 1, 2, 3
my_variable <- c(1,2,3)
my_variable

### Question 6

#  We go back to question 1 and compute directly:
4 * 512 + 3 * 768
7 * 20
24 * 64 + 4 * 192
24 * 20 + 4 * 16

### Question 7

#  We load in splash_mountain data and display the head:
splash_mountain <- read.csv("/class/datamine/data/disney/splash_mountain.csv")
head(splash_mountain)

### Question 8

#  Submit this R file, and an Rmd file, and the resulting pdf file.