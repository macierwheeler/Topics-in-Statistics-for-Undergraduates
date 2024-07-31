# Macie Wheeler
# Project 5

### Question 1

# creates data frame with accident info from 1975 - 1981 inclusive
accidents <- rbind(read.csv('/class/datamine/data/fars/1975/ACCIDENT.CSV'),
                   read.csv('/class/datamine/data/fars/1976/ACCIDENT.CSV'),
                   read.csv('/class/datamine/data/fars/1977/ACCIDENT.CSV'),
                   read.csv('/class/datamine/data/fars/1978/ACCIDENT.CSV'),
                   read.csv('/class/datamine/data/fars/1979/ACCIDENT.CSV'),
                   read.csv('/class/datamine/data/fars/1980/ACCIDENT.CSV'),
                   read.csv('/class/datamine/data/fars/1981/ACCIDENT.CSV'))

# changes the years to have 4 digits instead of 2
accidents$YEAR <- paste0('19', accidents$YEAR)

unique(accidents$YEAR)

### Question 2

# gives the number of accidents that involved one or more drunk drivers and
# a school bus
length(which((accidents$DRUNK_DR >= 1) & (accidents$SCH_BUS == 1)))

### Question 3

# creates a table with the amounts of these types of accidents for each year
table(accidents$YEAR[(accidents$DRUNK_DR >= 1) & (accidents$SCH_BUS == 1)])

# 1978 had the largest number of the qualifying accidents

### Question 4

# calculates the mean number of motorists that were involved in accidents with
# 0-6 drunk drivers
for (i in 0:6) {
  print(paste0("The mean number of motorists involved in an accident with ", i, 
               " drunk drivers is: ", mean(accidents$PERSONS[accidents$DRUNK_DR == i])))
}

### Question 5

# creates a new data frame with only the four states we want
midwestDF <- accidents[(accidents$STATE == 18) | (accidents$STATE == 17) |
                         (accidents$STATE == 39) | (accidents$STATE == 26), ]

# gives a stacked barplot of each states accidents for each month
barplot(table(midwestDF$STATE, midwestDF$MONTH), 
        legend = rownames(table(midwestDF$STATE, midwestDF$MONTH)), 
        main = 'Accidents for Indiana(18), Illinois(17), Ohio(39), and Michigan(26)
        Per Month', xlab = 'Months', ylab = 'Number of Accidents', col = 3:6,
        names.arg = c('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 
                      'Sept', 'Oct', 'Nov', 'Dec'))

# The summer months actually have the most accidents.
# I am surprised by these results because I figured in the winter when there
# is snow that there would be a lot more accidents. But maybe there are a lot
# or accidents in the summer due to rain and lots of people being out on the 
# roads.