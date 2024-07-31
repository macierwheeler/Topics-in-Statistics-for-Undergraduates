# Macie Wheeler
# Project 4

### Question 1

splash_mountain <- read.csv('/class/datamine/data/disney/splash_mountain.csv')

count <- 0
s <- 0

for (x in splash_mountain$SPOSTMIN) {
  if (is.na(x)) {
    # ignores NA values
    next
  } else if (x == -999) {
    # ignores -999 values
    next
  } else {
    # increases the count of rows used in SPOSTMIN
    # adds the value to the sum of the values of SPOSTMIN
    count <- count + 1
    s <- s + x
  }
}

s / count
# gives the average of the values from SPOSTMIN

# The mean posted wait time is 43.3892.

### Question 2

rock_n_rollercoaster <- read.csv('/class/datamine/data/disney/rock_n_rollercoaster.csv')

for (i in 1:nrow(rock_n_rollercoaster)) {
  if (any(rock_n_rollercoaster[i, c('SPOSTMIN', 'SACTMIN')] == -999, na.rm = T)) {
    # writes closed to new column status because SPOSTMIN or SACTMIN was -999, 
    # ignores NA values
    rock_n_rollercoaster$status[i] <- 'closed'
  } 
  else {
    # writes open to new column status because SPOSTMIN or SACTMIN wasn't -999
    rock_n_rollercoaster$status[i] <- 'open'
  }
}

rock_n_rollercoaster$status <- factor(rock_n_rollercoaster$status)
# changes the new status column into a column of factors instead of strings

str(rock_n_rollercoaster)

### Question 3

rock_n_rollercoaster <- read.csv('/class/datamine/data/disney/rock_n_rollercoaster.csv')

myStatus <- rep("open", times = nrow(rock_n_rollercoaster))
# assign every value in status as 'open'
myStatus[(rock_n_rollercoaster$SPOSTMIN == -999) | (rock_n_rollercoaster$SACTMIN == -999)] <- "closed"
# change correct values in status to 'closed' when SPOSTMIN and SACTMIN are -999

rock_n_rollercoaster$status <- factor(myStatus)
# adds values to the column status in the data frame

str(rock_n_rollercoaster)

# The method utilizing vectorized operations and indexing worked a lot faster
# than using a for loop.

### Question 4

splash_mountain <- read.csv('/class/datamine/data/disney/splash_mountain.csv')

myStatus <- rep("open", times = nrow(splash_mountain))
# assign every value in status as "open"
myStatus[(splash_mountain$SPOSTMIN == -999) | (splash_mountain$SACTMIN == -999)] <- "closed"
# change correct values in status to "closed" when SPOSTMIN and SACTMIN are -999

splash_mountain$status <- factor(myStatus)
# adds values to the column status in the data frame

statusCount <- table(splash_mountain$status)
# gets the count of number of "opens"'s and number of "closed"'s for Splash Mountain

pie(statusCount, main = "Splash Mountain: Number of Times the Ride was Open vs. Closed")

### Question 5

myPieChart <- function(x) {
  ride_files <- read.csv(paste0(c("/class/datamine/data/disney/"), x, ".csv"))
  # opens each ride file
  
  myStatus <- rep("open", times = nrow(ride_files))
  # assign every value in ride status as "open"
  myStatus[(ride_files$SPOSTMIN == -999) | (ride_files$SACTMIN == -999)] <- "closed"
  # change correct values in ride status to "closed" when SPOSTMIN and SACTMIN are -999
  
  ride_files$status <- factor(myStatus)
  # adds values to the column status in the data frame
  
  statusCount <- table(ride_files$status)
  # gets the count of number of "open"'s and number of "closed"'s for each ride
  
  pie(statusCount, main = x)
}

ride_names <- c("splash_mountain", "soarin", "pirates_of_caribbean", "expedition_everest", "flight_of_passage", "rock_n_rollercoaster")
par(mfrow=c(2,3))
# allows all the pie charts to be on the same page

for (ride in ride_names) {
  myPieChart(ride)
}
# loops through each ride name given in ride_names and create a pie chart for each