# Macie Rose Wheeler
# Project 2

### Question 1

myDF <- read.csv("/class/datamine/data/disney/metadata.csv")
head(myDF)

### Question 2

our_vec <- myDF$WDWMAXTEMP
our_vec[1]
our_vec[50]
typeof(our_vec)

#  The first value in the vector is 73.02.
#  The 50th value in the vector is 51.24.
#  The type of data in the vector is: double. 

### Question 3

first50 <- head(our_vec, n = 50)
first50

last50 <- tail(our_vec, n = 50)
last50

mymix <- first50 + last50
mymix

### Question 4

hot <- myDF$WDWMAXTEMP[myDF$WDWMAXTEMP >= 80]
length(hot)
hot + first50

#  Hot has 1255 elements.
#  When trying to calculate the sum of hot and first50 we do get a warning.
#  This is because first50 only contains 50 elements, whereas hot contains 1255.
#  R does a thing called recycling where the elements of first50 are recycled,
#  or repeated, until it's long enough to match the length of hot. R will do
#  this with no problem, but it will still throw an error.

### Question 5

plot(myDF$WDWMAXTEMP)

### Question 6

dat <- tapply(myDF$WDWMEANTEMP, myDF$DAYOFYEAR, mean, na.rm=T)
seasons <- tapply(myDF$SEASON, myDF$DAYOFYEAR, function(x) unique(x)[1])
pal <- c("#4E79A7", "#F28E2B", "#A0CBE8",  "#FFBE7D", "#59A14F", "#8CD17D",
         "#B6992D", "#F1CE63", "#499894", "#86BCB6", "#E15759", "#FF9D9A",
         "#79706E", "#BAB0AC", "#1170aa", "#B07AA1")
colors <- factor(seasons)
levels(colors) <- pal
par(oma=c(7,0,0,0), xpd=NA)
barplot(dat, main="Average Temperature", xlab="Jan 1 (Day 0) - Dec 31 (Day 365)",
        ylab="Degrees in Fahrenheit", col=as.factor(colors), border = NA, space=0)
legend(0, -30, legend=levels(factor(seasons)), lwd=5, col=pal, ncol=3, cex=0.8,
       box.col=NA)

#  This is my favorite graph because it has a very appealing and colorful visual.
#  It's interesting to see that the average temperatures throughout the year only
#  have about a 30-40 degree difference. I think the color selection could be
#  improved though, since it's hard to tell which color in the key corresponds
#  to which color in the actual graph.