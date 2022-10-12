# How to use build in datasets of R
data() # all datasets in R
View(CO2) # To view datasets in R console

View(PlantGrowth) 

View(iris)

View(Titanic)

View(mtcars)

View(trees)

View(npk) # NPK data for factorial design

head(CO2) # to show first 6 rows of  data
names(CO2) # to show the names of columns
nrow(CO2) # to show number of rows
ncol(CO2) # to show number of columns

install.packages("writexl") # to save  .xlsx files
library(writexl)

write_xlsx(CO2,path="D:\\Data Science\\R_with_BaBaG\\CO2.xlsx") 

library(ggplot2) # to plot graphs and figures

ggplot(trees, aes(Girth, Height))+geom_point(size=3)+geom_smooth(method="lm") # scatter plot

