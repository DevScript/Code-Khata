# How to install pacakges?----
#install.packages("readr") #installing package
library(readr) #reading package to activate or use it
require(readr) # to activate or use package


#install.packages("readxl") #installing package
library(readxl) #reading package to activate or use it
#install.packages("ggplot2") #installing package
library(ggplot2) #reading package to activate or use it
#install.packages("tidyverse") #installing package
library(tidyverse) #reading package to activate or use it
#install.packages("tidyr") #installing package
library(tidyr) #reading package to activate or use it
#install.packages("agricolae") #installing package
library(agricolae) #reading package to activate or use it
#install.packages("multcomp") #installing package
library(multcomp) #reading package to activate or use it
#install.packages("dplyr")
library(dplyr) #reading package to activate or use it




# Built-in datasets of R----

data() #to view list of datasets
data("iris")
tibble(iris)






## Basic R functions----
#1- Scatter plot
plot(iris) #worst practice
plot(iris$Sepal.Length)
#For sepal
plot(x = iris$Sepal.Length,y=iris$Sepal.Width)

# For petal
plot(x = iris$Petal.Length,y=iris$Pepal.Width)

#2- Histogram
# for petal
hist(x = iris$Petal.Length)
hist(x = iris$Petal.Width)

#For sepal
hist(x = iris$Sepal.Length)
hist(x = iris$Sepal.Width)

#3- Stripchart
#for sepal
stripchart(iris$Sepal.Length ~ iris$Sepal.Width)
#for petal
stripchart(iris$Petal.Length ~ iris$Petal.Width)

#4- qqnorm plot
# for sepal
qqnorm(iris$Sepal.Length)
# for petal
qqnorm(iris$Petal.Length)

#5- barplot
# For sepal
barplot(iris$Sepal.Length)
# For Petal
barplot(iris$Petal.Length)

#6- mosaic plot
# For sepal
mosaicplot(~ iris$Sepal.Length+iris$Sepal.Width)
# For Petal
mosaicplot(~ iris$Sepal.Length+iris$Sepal.Width)
