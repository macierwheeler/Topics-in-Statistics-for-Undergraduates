# Macie Wheeler
# Project 6

### Question 1

dat <- read.csv('/class/datamine/data/fars/7581.csv')

# Read in data that maps state codes to state names
state_names <- read.csv("/class/datamine/data/fars/states.csv")
# Create a vector of state names called v
v <- state_names$state
# Set the names of the new vector to the codes
names(v) <- state_names$code
# Create a new column in the dat dataframe with the actual names of the states
dat$mystates <- v[as.character(dat$STATE)]


# The mean number of motorists involved in accidents by number of drunk drivers.
tapply(dat$PERSONS, dat$DRUNK_DR, mean)

# I preferred the tapply method since it was a lot easier and faster to type out.

### Question 2

# The mean number of drunk drivers per accident by state.
sort(tapply(dat$DRUNK_DR, dat$mystates, mean))

# New Hampshire has the highest average number of drunk drivers per accident.

### Question 3

# The sum of total number of fatalities by day of the week.
sort(tapply(dat$FATALS, dat$DAY_WEEK, sum))

# The numbers aren't too surprising to me since Saturday has the highest number
# of fatalities, Sunday has the second highest number of fatalities, and Friday has
# the third highest number of fatalities. I expected more fatalities on the weekend
# days since more people are going out or traveling, and it's more likely that
# there are drunk drivers out on the weekends.

# I would expect the proportions of fatalities over the total number of people in
# the accidents to be higher on days like Tuesday, Monday, and Wednesday. This is 
# because those were the days that had the smaller amounts of fatalities, which
# I would expect to have close to the same number of people involved in the accidents
# making those proportions closer to 1 and therefore larger.

# Proportion of fatalities over the total number of people in the accidents.
sort(tapply(dat$FATALS, dat$DAY_WEEK, sum) / tapply(dat$PERSONS, dat$DAY_WEEK, sum))

# My expectation was slightly off since Thursday actually had the highest proportion,
# however Wednesday was second highest, Tuesday was third highest, and Monday was
# fourth highest.

### Question 4

# Average of how many drunk drivers are involved in accidents by type of road.
tapply(dat$DRUNK_DR, dat$ALIGNMNT, mean)

# On average about 31.4% of drunk drivers are involved in crashes on straight roads.
# On average about 47.3% of drunk drivers are involved in crashes on curved roads.

# Question 5

# Total number of fatalities that occur during each of the time intervals.
tapply(dat$FATALS, cut(dat$HOUR, breaks = c(0, 6, 12, 18, 24, 99), include.lowest = T), sum)

# Average number of fatalities that occur during each of the time intervals.
tapply(dat$FATALS, cut(dat$HOUR, breaks = c(0, 6, 12, 18, 24, 99), include.lowest = T), mean)
