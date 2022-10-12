library(readxl)
my_data <- read_excel("D:/Data Science/R_with_BaBaG/MLR_Salary.xlsx")
View(my_data)

remove(MLR_Salary)

boxplot(my_data$age ~ my_data$Salary)

# labeling
boxplot(age ~ Salary,data=my_data)

boxplot(age ~ Salary,data=my_data,main="Boxplot of Experiment",xlab="Salary",ylab="Age")

#coloring
boxplot(age ~ Salary,data=my_data,main="Boxplot of Experiment",xlab="Salary",ylab="Age",col="Red",border="grey")

#grouping of treatment
my_data2Age <- factor(my_data$Age, levels = c(21, 26, 30, 36, 41))

boxplot(my_data$age ~ my_data$Salary * my_data$YearsExperience)

