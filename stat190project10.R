# Macie Wheeler
# Project 10

### Question 1

users <- read.csv('/class/datamine/data/okcupid/filtered/users.csv')
questions <- read.csv('/class/datamine/data/okcupid/filtered/questions.csv', sep = ';')

# The users file looks like it contains the question number for each question and
# the answers for each of those questions depending on what the user chose,
# the traits that someone can pick from to explain themselves (or to specify what
# they're looking for), and the option to choose gender/gender orientation and race.

# The questions file looks like it contains each question and its number, the 
# options available for each question, a count of some sort (maybe how many people have
# answered that question), and keywords for that question.

# These files are related since each of the questions in the questions file is
# in the users file with the counts of how many people chose which option to 
# answer the question.

### Question 2

questions[grep('google', questions$text, ignore.case = TRUE), ]

# The question is "Do you Google someone before a first date?".

### Question 3

prop.table(table(users$q170849, useNA = 'always'))

# The percentage of users that Google someone before the first date is about 20%.

tapply(users$q170849, users$gender2, function(x) {prop.table(table(x, useNA = 'always'))})

# The proportion does change a little bit by gender when specified by gender2.
# For men the proportion that Google someone before the first date is about 18.8%.
# For women the proportion that Google someone before the first date is about 21.8%.

tapply(users$q170849, users$gender_orientation, function(x) {prop.table(table(x, useNA = 'always'))})

# The proportion also changes a little by gender when specified by gender_orientation.
# Bisexual males and females both have a proportion of about 24% for Googling
# someone before the first date.
# Heterosexual males and gay females both have a proportion of about 18% for Googling
# someone before the first date.
# Gay males have the highest proportion for Goggling someone before the first date
# at about 29%.
# Heterosexual females have a proportion of about 21.5% for Googling someone before
# the first date.

### Question 4

count_words <- function(my_text) {
  my_split_text <- unlist(strsplit(my_text, " "))
  
  return(length(my_split_text[my_split_text!=""]))
}

questions$question_length <- sapply(questions$text, count_words)

str(questions)

### Question 5

number_of_options <- function(myDF) {
  table(apply(as.matrix(myDF[ ,3:6]), 1, function(x) {sum(!(x==""))}))
}

my_list <- split(questions, questions$Keywords)

sapply(my_list, number_of_options)

### Question 6

questions$text[234]

table(users$gender2)

my_results <- tapply(users$q366, users$gender2, function(x) {prop.table(table(x, useNA = 'always'))})

par(mfrow = c(2, 1))
sapply(1:2, function(x) {barplot(my_results[[x]], main = names(my_results)[x])})

# My analysis gets the proportion of users by their gender and their
# answer to the question 'When you're not in a serious relationship, what do you
# prefer?'.
# It then creates a barplot of those proportions per answer option per gender.
# I'd expected that women would have a higher proportion of answering the question
# 'Dating one person at a time', however men actually had a higher percentage
# at about 30%, whereas women had a percentage of about 19%.