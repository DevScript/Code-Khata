# was not able to found cordblood data so applying those things on iris dataset
# laoding data----
data("iris")




# a.----
# calling 6 rows of data----
head(iris)
# all are continous except Species column

# b. -----
 # histograms of numeric columns
hist(iris$Sepal.Length) # symmetric
hist(iris$Sepal.Width) # proper historgram bell shape
hist(iris$Petal.Length) # negative skewed
hist(iris$Petal.Width)  # negative skewed

 # box plots

boxplot(iris$Sepal.Length) # positive skewed
boxplot(iris$Sepal.Width) # some outliers and negative skewed
boxplot(iris$Petal.Length) # positive skewed 
boxplot(iris$Petal.Width) # positive skewed

boxplot(iris$Petal.Length,iris$Petal.Width)
boxplot(iris$Sepal.Length,iris$Sepal.Width)

boxplot(iris$Species,iris$Sepal.Width)


# c. ----
summary(iris) # summary of df
# yes cuz we are working on it only