library(readxl)
data <- read_excel("D:/Data Science/R_with_BaBaG/MLR_Salary.xlsx", 
                   col_types = c("numeric", "numeric", "numeric", 
                                 "numeric"))
View(data)

# mean
mean(data$age)
mean(data$YearsExperience)

#median
median(data$age)
median(data$Salary)

#min
min(data$age)

#max
max(data$age)

#range
range(data$age)

#quantile
quantile(data$Salary, .25)
quantile(data$Salary, .50)
quantile(data$Salary, .75)

#standard deviation
sd(data$age)

#variance
var(data$age)

# apply operation over 2 columns at same time
lapply(data[,2:3],mean)
lapply(data[,2:3],sd)
lapply(data[,2:3],var)

# summary
summary(data)

# anova
aov(data$age ~ data$Salary)

a1 <- aov(data$age ~ data$Salary)
summary(a1)

# tukey HDS
TukeyHSD(a1)
 
#group anova
a2 <- aov(data$age ~ data$YearsExperience)
summary(a2)

TukeyHSD(a2)


