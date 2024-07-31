# Macie Wheeler
# Project 3

### Question 1

splash_mountain <- data.frame(read.csv('/class/datamine/data/disney/splash_mountain.csv'))
dim(splash_mountain)

# There are 223936 rows and 4 columns in the dataset.

### Question 2

mean(splash_mountain$SPOSTMIN, na.rm = T)
sd(splash_mountain$SPOSTMIN, na.rm = T)

# The average posted minimum wait time for Splash Mountain is -71.70373.
# The standard deviation is 328.0586.

# Given the values we can see in the SPOSTMIN column of the Splash Mountain data
# the average does not seem to make sense since it's negative. However, there
# must be negative posted minimum wait times farther down in the data frame. The
# standard deviation also looks very high, but if there were negative values
# farther in the data frame then it would make sense.

### Question 3

mean(splash_mountain$SPOSTMIN[splash_mountain$SPOSTMIN != -999], na.rm = T)
sd(splash_mountain$SPOSTMIN[splash_mountain$SPOSTMIN != -999], na.rm = T)

# The average posted minimum wait time for Splash Mountain without the values
# -999 is now 43.3892.
# The standard deviation without the values -999 is now 31.74894.
# Getting rid of the -999 values seems to have fixed our problems and the average
# and standard deviation now look a lot more reasonable.

### Question 4

colnames(splash_mountain)[which(colnames(splash_mountain) == "SPOSTMIN")] <- "posted_min_wait_time"
colnames(splash_mountain)[which(colnames(splash_mountain) == "SACTMIN")] <- "actual_wait_time"

colnames(splash_mountain)

### Question 5

quarter <- cut(as.Date(splash_mountain$date, "%m/%d/%Y"), "quarter")

levels(quarter) <- paste0("q", 1:nlevels(quarter))

splash_mountain$quarter <- quarter

head(splash_mountain)
tail(splash_mountain)

nlevels(quarter)
# There are 20 quarters.

### Question 6

# I acknowledge that the STAT 19000/29000/39000 1-credit Data Mine seminar
# will be recorded and posted on Piazza, for participants in this course.