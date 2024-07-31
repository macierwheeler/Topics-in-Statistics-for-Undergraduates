# Macie Wheeler
# Project 11

### Question 1

zipc <- read.csv('/class/datamine/data/zillow/Zip_time_series.csv',
                 colClasses = c('RegionName' = 'character'))

head(zipc$RegionName)

### Question 2

mean_median_listing <- mean(zipc$MedianListingPrice_AllHomes, na.rm = TRUE)
mean_ZHVI <- mean(zipc$ZHVI_AllHomes, na.rm = TRUE)

mean_median_listing - mean_ZHVI

# On average the median listing price is $80,926.02 higher than the Zillow Home
# Value Index. This result would make sense since many people try to list their
# house for a higher price than what it's actually worth a lot of the time. Another
# potential reason for this is since the median listing price column contains a lot
# of NA values the mean of that column is going to be bigger than normal since it's
# not being divided by as many numbers. This will make the mean of the median listing 
# prices greater than the mean of the Zillow Home Value Indexes, since that column 
# doesn't have as many NA values as the median listing prices.

### Question 3

table(format(as.Date(zipc$Date, format = "%Y-%m-%d"), "%Y"))

# There are 22 years of data in this dataset.

myYears <- format(as.Date(zipc$Date, format = "%Y-%m-%d"), "%Y")

mean_median_lising_by_years <- tapply(zipc$MedianListingPrice_AllHomes, myYears,
                                      mean, na.rm = TRUE)
mean_ZHVI_by_years <- tapply(zipc$ZHVI_AllHomes, myYears, mean, na.rm = TRUE)

plot(1996:2017, mean_median_lising_by_years, ylim = c(0, 400000), col = 'red',
     ylab = 'Average', xlab = 'Year', main = 'Average MedianListingPrices_AllHomes
     and Average ZHVI_AllHomes')
lines(1996:2017, mean_median_lising_by_years, ylim = c(0, 400000), col = 'red')
par(new = TRUE)
plot(1996:2017, mean_ZHVI_by_years, ylim = c(0, 400000), col = 'blue',
     ylab = 'Average', xlab = 'Year', main = 'Average MedianListingPrices_AllHomes
     and Average ZHVI_AllHomes')
lines(1996:2017, mean_ZHVI_by_years, ylim = c(0, 400000), col = 'blue')
abline(v="2008", lty="dotted")
legend('topleft', c('MedianListingPrices_AllHomes', 'ZHVI_AllHomes'), fill = c('red', 'blue'))

### Question 4

states = read.csv('/class/datamine/data/zillow/State_time_series.csv',
                  colClasses = c('RegionName' = 'character'))

states$RegionName[states$RegionName == 'DistrictofColumbia'] = 'District of Columbia'
states$RegionName = trimws(gsub('([a-z])([A-Z])', '\\1 \\2', states$RegionName))

mean_median_listing_by_region <- tapply(states$MedianListingPrice_AllHomes,
                                       states$RegionName, mean, na.rm = TRUE)

mean_median_listing_by_states <- mean_median_listing_by_region[names(mean_median_listing_by_region)
                                                               %in% state.name]

datamine_py()
library(usmap)

plot_usmap(regions = 'states', data = data.frame(state = names(mean_median_listing_by_states), 
           myvalues = mean_median_listing_by_states), values = 'myvalues')

### Question 5

counties <- read.csv('/class/datamine/data/zillow/County_time_series.csv',
                     colClasses = c('RegionName' = 'character'))

mean_ZRI_by_county <- tapply(counties$ZRI_AllHomes, counties$RegionName, mean, na.rm = TRUE)
plot_usmap(regions = 'counties', data = data.frame(fips = names(mean_ZRI_by_county),
            myvalues = mean_ZRI_by_county), values = 'myvalues')
