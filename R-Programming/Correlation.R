# Install packages----
install.packages("psych")
install.packages("corrplot")
install.packages("RColorBrewer")
library(psych)
library(corrplot)
library(RColorBrewer)



#pysch package----
data("iris")
x <- corr.test(iris[-5])
x
pairs.panels(iris[-5])



#import dataset or use iris----
x1 <-iris

m <- cor(x1[-5])

corrplot(m)

?corrplot

corrplot(m, type="upper")

corrplot(m, type="lower")

corrplot(m, type="lower", order="hclust")

corrplot(m, type="upper", order="hclust",method="pie")

corrplot(m, type="upper", order="hclust",method="ellipse")

corrplot(m, type="upper", order="hclust",method="square")

corrplot(m, type="upper", order="hclust",method="shade")

corrplot(m, type="upper", order="hclust",method="number")

corrplot(m, type="upper", order="hclust",method="number",col=brewer.pal(n=8,name="RdYlBu"))

#mixed plot
corrplot.mixed(m)

corrplot.mixed(m,lower.col="black",number.cex=0.8)


corrplot.mixed(m, lower="square",upper="pie",tl.col="Red")

m1 <- cor(x1[-5],method="pearson")

m2 <- cor(x1[-5],method="spearman")
