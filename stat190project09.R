# Macie Wheeler
# Project 9

### Question 1

library(imager)

books <- read.csv("/class/datamine/data/goodreads/csv/goodreads_books.csv")
authors <- read.csv("/class/datamine/data/goodreads/csv/goodreads_book_authors.csv")

get_author_name <- function(my_authors_dataset, my_author_id){
  return(my_authors_dataset[my_authors_dataset$author_id==my_author_id,'name'])
}

fun_plot <- function(my_authors_dataset, my_books_dataset, my_book_id, display_cover=T) {
  book_info <- my_books_dataset[my_books_dataset$book_id==my_book_id,]
  all_books_by_author <- my_books_dataset[my_books_dataset$author_id==book_info$author_id,]
  author_name <- get_author_name(my_authors_dataset, book_info$author_id)
  
  img <- load.image(book_info$image_url)
  
  if(display_cover){
    par(mfrow=c(1,2))
    plot(img, axes=FALSE)
  }
  
  plot(all_books_by_author$num_pages, all_books_by_author$average_rating, 
       ylim=c(0,5.1), pch=21, bg='grey80',
       xlab='Number of pages', ylab='Average rating', 
       main=paste('Books by', author_name))
  
  points(book_info$num_pages, book_info$average_rating,pch=21, bg='orange', cex=1.5)
}

# The function is called fun_plot and it takes four arguments: my_authors_dataset, 
# my_books_dataset, my_book_id, and display_cover.

fun_plot(authors, books, 287149, display_cover = TRUE)
fun_plot(authors, books, 19545936, display_cover = TRUE)

# This function basically finds the book that corresponds to the book id that
# you input in as the argument. It then prints the image of the cover of the book if 
# specified.
# It also finds all of the books by the author of the book id and graphs a plot
# of the total number of pages for each of the author's books by the average rating
# for each of the author's books as grey dots. Within the plot there is an orange dot for the
# chosen book id's number of pages vs. its average rating.
# The function gives you an option as to whether or not you want to display the cover.

### Question 2

fun_plot2 <- function(my_authors_dataset, my_books_dataset, my_book_id, display_cover=T) {
  
  if(sum(my_books_dataset$book_id == my_book_id) == 0) {
    stop('Book ID not found.')
  } 
  else {
    book_info <- my_books_dataset[my_books_dataset$book_id==my_book_id,]
    all_books_by_author <- my_books_dataset[my_books_dataset$author_id==book_info$author_id,]
    author_name <- get_author_name(my_authors_dataset, book_info$author_id)
    
    img <- load.image(book_info$image_url)
    
    if(display_cover){
      par(mfrow=c(1,2))
      plot(img, axes=FALSE)
    }
    
    plot(all_books_by_author$num_pages, all_books_by_author$average_rating, 
         ylim=c(0,5.1), pch=21, bg='grey80',
         xlab='Number of pages', ylab='Average rating', 
         main=paste('Books by', author_name))
    
    points(book_info$num_pages, book_info$average_rating,pch=21, bg='orange', cex=1.5)
  }
}

fun_plot2(authors, books, 123, display_cover = TRUE)
fun_plot2(authors, books, 19063, display_cover = TRUE)

### Question 3

get_author_id <- function(my_authors_dataset, my_author_name) {
  return(my_authors_dataset[my_authors_dataset$name == my_author_name, 'author_id'])
}

get_author_id(authors, "Brandon Sanderson")
get_author_id(authors, "J.K. Rowling")

### Question 4

search_books_for_word <- function(word, my_books_dataset) {
  return(books[grepl(word, my_books_dataset$description, fixed=T),]$title)
}

search_books_for_word('mystery', books)

### Question 5

compare_number_of_books_between_two_authors <- function(my_books_dataset, my_authors_dataset, author_id_1, author_id_2) {
  author_1_books <- length(my_books_dataset$title[my_books_dataset$author_id == author_id_1])
  author_1 <- my_authors_dataset[my_authors_dataset$author_id == author_id_1, 'name']
  author_2_books <- length(my_books_dataset$title[my_books_dataset$author_id == author_id_2])
  author_2 <- my_authors_dataset[my_authors_dataset$author_id == author_id_2, 'name']
  
  barplot(c(author_1_books, author_2_books), width = 1,
          names.arg = c(paste0(author_1, ' Books'), paste0(author_2, ' Books')),
          col = c('mistyrose', 'lightcyan'), xlab = 'Authors',
          ylab = 'Number of Books Each Author Has',
          main = 'Barplot of Number of Books Between Two Different Authors')
}

compare_number_of_books_between_two_authors(books, authors, 137561, 53088)
compare_number_of_books_between_two_authors(books, authors, 19739, 15104629)