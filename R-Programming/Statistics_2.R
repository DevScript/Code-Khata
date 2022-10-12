library(readxl)
x <- read_excel("D:/Data Science/R_with_BaBaG/MLR_Salary.xlsx")
View(x)

# boxplot
boxplot(x$age ~ x$YearsExperience)
boxplot(age ~ YearsExperience, data=x)
# multiple mean test --> for 2 --> t-test
# for more than 2 --> tukey 

#1- Tukey-HSD (host significant differnece) test

install.packages("agricolae")
library(agricolae)

help("agricolae-package")
?'agricolae-package'

model <- aov(age ~ YearsExperience, data=x)
out <- HSD.test(model, "YearsExperience", group=TRUE,main="Tukey Test")
plot(out)

#2- LSD.test
model1 <- aov(age ~ YearsExperience, data=x)
out1 <- LSD.test(model1, "YearsExperience", group=TRUE,main="Tukey Test")
plot(out1)

#3- Ducan test
model2 <- aov(age ~ YearsExperience, data=x)
out2 <- duncan.test(model2, "YearsExperience", group=TRUE,main="Tukey Test")
plot(out2)

#grouping
boxplot(age ~ Salary * YearsExperience,  data = x)

model3 <- aov(age ~ Salary * YearsExperience,  data = x)
out3 <- HSD.test(model3, c("Salary","YearsExperience"), group=TRUE,main="Tukey Test")
plot(out3)
plot(out3, horiz=TRUE)
plot(out3, las=2)

# String = "Crop" or "water"

jpeg(file="Tukey test.tiff",width=6,height=4, units="in",res=300)
boxplot(age ~ Salary * YearsExperience,  data = x, las=2,xlab="")
dev.off()