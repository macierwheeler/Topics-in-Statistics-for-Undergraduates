# Macie Wheeler
# Project 12

### Question 1

states <- read.csv('/class/datamine/data/zillow/State_time_series.csv')

library(lubridate)

class(states$Date)
typeof(states$Date)

# Both the class and type of the column Date is character.

### Question 2

states$Date <- ymd(states$Date)

class(states$Date)

# The class of the modified Date column is Date.

# This as.Date method that we used in the last project takes in how we want the
# date to be formatted in the end, whereas the lubridate methods just use the 
# format of how the date is now and puts it into a new date format. Both the
# methods outputted the date in the same format. I personally
# like the lubridate methods better because we can easily see how the date is 
# currently formatted and there is less code to write out.

### Question 3

states$year <- year(states$Date)
states$month <- month(states$Date)
states$day_of_week <- wday(states$Date, label = TRUE)

table(states$year, states$month, states$day_of_week)

# The data seems to have roughly the same amount for all years, all months, and
# all days of the week.
# I prefer the lubridate method over the method we used in the previous project 
# for getting the years, months, and days of the week. The lubridate methods are
# quick and easy to use.

### Question 4

barplot(tapply(states$DaysOnZillow_AllHomes, states$month, mean, na.rm = TRUE),
        main = 'Average Days on Zillow (All Homes) for All Months', xlab = 'Month',
        ylab = 'Average Days on Zillow', names.arg = month.abb)

# Based on the barplot it seems as if July is the best month to put your house
# on the market since it has the lowest average number of days on zillow.

### Question 5

states2010plus <- states[states$year >= 2010, ]

plot(tapply(states2010plus$DaysOnZillow_AllHomes, states2010plus$Date, mean,
            na.rm = TRUE), type = 'l', ylab = 'Average Days on Zillow', main =
       'Average Days on Zillow (All Homes) for Years 2010+ by Date', xlab = 'Date')

# I notice that as the dates get farther into the future the average number of days
# that all of the homes are on Zillow for decreases. However, the data decreases
# in an up and down pattern, a.k.a it decreases, then increases, then decreases,
# but in an overall decrease. This might make some more sense since as there years
# go on more people seem to be buying homes as the population of the United States
# gets bigger every year.

### Question 6

california <- subset(states2010plus, RegionName == 'California')
indiana <- subset(states2010plus, RegionName == 'Indiana')
newyork <- subset(states2010plus, RegionName == 'NewYork')
florida <- subset(states2010plus, RegionName == 'Florida')


plot(tapply(california$DaysOnZillow_AllHomes, california$Date, mean, na.rm = TRUE),
     ylab = 'Average Days on Zillow', main = 'Average Days on Zillow (All Homes)
     for Years 2010+ by Date for Four States', xlab = 'Date', type = 'l', col = 'blue',
     ylim = c(50, 220))
par(new = TRUE)
plot(tapply(indiana$DaysOnZillow_AllHomes, indiana$Date, mean, na.rm = TRUE),
     ylab = 'Average Days on Zillow', main = 'Average Days on Zillow (All Homes)
     for Years 2010+ by Date for Four States', xlab = 'Date', type = 'l', col = 'red',
     ylim = c(50, 220))
par(new = TRUE)
plot(tapply(newyork$DaysOnZillow_AllHomes, newyork$Date, mean, na.rm = TRUE),
     ylab = 'Average Days on Zillow', main = 'Average Days on Zillow (All Homes)
     for Years 2010+ by Date for Four States', xlab = 'Date', type = 'l', col = 'green',
     ylim = c(50, 220))
par(new = TRUE)
plot(tapply(florida$DaysOnZillow_AllHomes, florida$Date, mean, na.rm = TRUE),
     ylab = 'Average Days on Zillow', main = 'Average Days on Zillow (All Homes)
     for Years 2010+ by Date for Four States', xlab = 'Date', type = 'l', col = 'purple',
     ylim = c(50, 220))
legend('topright', legend = c('California', 'Indiana', 'New York', 'Florida'),
       fill = c('blue', 'red', 'green', 'purple'), )

# Homes do see to sell faster in some states, since New York's average days on
# Zillow is a lot higher than California's, which means the homes in California
# are selling a lot faster. I'm not too surprised that the average days on Zillow
# for both Indiana and Florida are relatively the same.
