library(readxl)
my_data <- read_excel("D:/Data Science/R_with_BaBaG/MLR_Salary.xlsx", 
                      col_types = c("numeric", "numeric", "numeric", 
                                    "numeric"))
View(my_data)

str(my_data)

head(my_data)
tail(my_data)

plot(my_data)

boxplot(my_data$age, my_data$Salary)
boxplot(my_data$YearsExperience, my_data$Salary)

boxplot(my_data$age ~ my_data$distance)
