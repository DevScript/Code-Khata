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





# How to update a pacakge-----
update.packages(ask=FALSE)


# How to update R via Rstudio?----
# Step1
install.packages("installr")
library(installr)

updateR()



# Repositories----
#1- CRAN -"Comprehensive R archive network"
#2- Github
install.packages("remotes")
library(remotes)
install_



# How to use help or documentation----
help("install_cran")



help("ggplot2") # to get documentation or its working


# How to set directories----
getwd() # working directory
setwd("path") # to set working directory



#how to read a file and work with it----
library(readxl)
year_df <- read_excel("D:/Data Science/R_with_BaBaG/year_df.xlsx", 
                      col_types = c("numeric", "numeric", "text"))
View(year_df)


str(year_df) # info of data
summary(year_df) # summary of data
tibble(year_df) # view data in good form
plot(year_df)



sum(year_df$num_of_papers) # to sum number of columns

# number of papers plot and their distribution
plot(year_df$num_of_papers) 
