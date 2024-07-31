# Macie Wheeler
# Project 8

### Question 1

books <- read.csv('/class/datamine/data/goodreads/csv/goodreads_books.csv')
authors <- read.csv('/class/datamine/data/goodreads/csv/goodreads_book_authors.csv')

# A function that, given a string (myColumn), returns the string
# without any punctuation.
strip_punctuation <- function(myColumn) {
  # Use regular expressions to identify punctuation.
  # Replace identified punctuation with an empty string ''.
  desc_no_punc <- gsub('[[:punct:]]+', '', myColumn)
  
  # Return the result
  return(desc_no_punc)
}

# The function has 1 argument myColumn. The function's name is strip_punctuation.

books$description <- strip_punctuation(books$description)

### Question 2

test_string <- "This is  a test string  with no punctuation"

words <- strsplit(test_string, " ")
unlistedWords <- unlist(words)
length(unlistedWords)

# The count of the words given by the strsplit function for our test_string is 
# not accurate, since there are spaces between words in our test_string that are
# bigger than one space. So, if we only split by one space, we are going to get
# empty strings in our words returned. There originally were 8 words, but using
# strsplit by spaces gave us 10 words.

### Question 3

whichWords <- which(unlistedWords != "")
length(whichWords)

### Question 4

count_words <- function(description) {
  
  words <- strsplit(description, " ")
  unlistedWords <- unlist(words)
  whichWords <- which(unlistedWords != "")
  length(whichWords)
  
}

count_words(books[2, "description"])

### Question 5

# Gives a 95% confidence interval of the true mean of the given data.
confidence_interval <- function(data) {
  
  t.test(x = data, conf.level = .95)$conf.int

}

confidence_interval(books$num_pages)
