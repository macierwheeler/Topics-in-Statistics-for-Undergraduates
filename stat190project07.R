# Macie Wheeler
# Project 7

### Question 1

books <- read.csv('/class/datamine/data/goodreads/csv/goodreads_books.csv')
authors <- read.csv('/class/datamine/data/goodreads/csv/goodreads_book_authors.csv')

dim(books)
dim(authors)

# There are 1000000 rows and 26 columns in the books dataset.
# There are 829529 rows and 5 columns in the authors dataset.

### Question 2

book_size <- cut(books$num_pages, breaks = c(0, 250, 500, 1000, Inf), 
                 labels = c('small', 'medium', 'large', 'huge'), include.lowest = TRUE)
table(book_size)

### Question 3

tapply(books$average_rating, book_size, mean)
tapply(books$text_reviews_count, book_size, mean)
tapply(books$publication_year, book_size, mean, na.rm = TRUE)

# I am surprised that the mean of the average ratings by book size is largest
# for the huge books. I thought people would like books that are shorter and 
# don't take as much time to read.
# I am also surprised that the mean of the text reviews count by book size is
# largest for the large books. I thought that it would be easier for people to
# review short books since they can read them faster.
# I am not surprised about the mean of the publication years by book size.
# A lot of larger books were written earlier on, since TV's and phones weren't as
# popular or didn't necessarily exist, and books were a good form of entertainment.

### Question 4

books_by_size <- split(data.frame(books$average_rating, books$text_reviews_count, books$publication_year), book_size)
class(books_by_size)

# The class of the results is a list.

lapply(books_by_size, colMeans, na.rm = TRUE)

### Question 5

en_books <- books[books$language_code %in% c("en-US", "en-CA", "en-GB", "eng", "en", "en-IN")
                  & books$publication_year > 2000, c("author_id", "book_id", "average_rating",
                  "description", "title", "ratings_count", "language_code", "publication_year")]

res<- subset(books, subset = (language_code %in% c("en-US", "en-CA", "en-GB", "eng", "en", "en-IN"))
             & (publication_year > 2000), select = c("author_id", "book_id", "average_rating",
             "description", "title", "ratings_count", "language_code", "publication_year"))

dim(en_books)
dim(res)

# The dimensions of en_books and res don't agree. They both have 8 columns, however
# en_books has 325499 rows and res has 243269 rows. en_books has NA values in
# its rows, but res doesn't. That's most likely why res has a smaller number
# of rows, since subset is getting rid of rows with NAs.

### Question 6

mymergedDF <- merge(res, authors, by="author_id")
dim(mymergedDF)

### Question 7 

listOfBooks <- mymergedDF$title[mymergedDF$name == 'Ray Bradbury']
listOfRatings <- mymergedDF$ratings_count.x[mymergedDF$name == 'Ray Bradbury']

listOfBooks[which.max(listOfRatings)]

# The title of the highest book from Ray Bradbury is "The Illustrated Man".
# I have never read Ray Bradbury's "The Illustrated Man", so I don't necessarily
# agree with it being his highest rated book, since in high school we were required
# to read "Farenheit 451" as I'm pretty sure most other high school students are.
# Knowing this, I'd think that there would be a lot more ratings for that book, 
# I also really enjoyed "Farenheit 451" and thought it was a well written book.