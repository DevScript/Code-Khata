library(readxl)
my_data <- read_excel("D:/Data Science/R_with_BaBaG/MLR_Salary.xlsx")
View(my_data)

# Comment
#strip chart
stripchart(my_data$age)
stripchart(my_data$age ~ my_data$YearsExperience)

# histogram
hist(my_data$age)
hist(my_data$YearsExperience)

#scatter plot
plot(my_data$age, my_data$Salary)

#qqnorm plot
qqnorm(my_data$age)

#barplot
barplot(my_data$age)

#mosaic plot
mosaicplot(~ my_data$age+my_data$distance)

