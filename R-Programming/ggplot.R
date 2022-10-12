install.packages("ggplot2")
library(ggplot2)

# ggplot (function)
# data (data1)
# mapping (xaxis, yaxis)
# geometry (scatter, box, line)

library(readxl)
x <- read_excel("MLR_Salary.xlsx")
View(ggdata)

ggplot(data=x, mapping=aes(x=age,y=YearsExperience))+ geom_point()

ggplot(x, aes(age,YearsExperience))+ geom_point()


ggplot(x, aes(age,YearsExperience))+ geom_point()+ geom_line()

ggplot(x, aes(age,YearsExperience))+ geom_point(size=3)+ geom_line()

ggplot(x, aes(age,YearsExperience))+ geom_point(size=3)+ geom_line(size=2)

ggplot(x, aes(age,YearsExperience))+ geom_boxplot()+ geom_point(size=3,color="red",alpha=0.3)

ggplot(x, aes(age,YearsExperience,color=Salary)) + geom_boxplot()

ggplot(x, aes(age,YearsExperience,color=Salary)) + geom_boxplot() + facet_wrap(-fert.type)

ggplot(x, aes(age,YearsExperience,color=Salary)) + geom_boxplot() + facet_wrap(-fert.type) +labs(x="Age",y="YearsExperience",title="Growth")+ theme_bw()+ggsave("ggplot1.tiff", units="in",width=8,height=6,dpi=300,compression='lzw')


