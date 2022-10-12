#read your data file
data("iris")

#principal component analysis
iris.pca <- prcomp(iris[, -5], center=TRUE, scale.= TRUE)
print(iris.pca)
summary(iris.pca)

#ggplot2 and grouping
iris <- cbind(iris, iris.pca$x)
ggplot(iris, aes(PC1, PC2, col = Species, fill = Species)) +
  stat_ellipse(geom = "polygon", col = "black", alpha = 0.5) +
  geom_point(shape = 21, col = "black")

#install packages for PCA analysis 
#install.packages("factoextra")
#install.packages("FactoMineR")
library(factoextra)
library(FactoMineR)

# create a principle component table
iris.pca1 <- PCA(iris[, -5], graph=TRUE, scale.unit = TRUE)

#to present most of the data screeplot
fviz_eig(iris.pca1, addlabels = TRUE, ylim=c(0,80))

#create a correlation plot
fviz_pca_var(iris.pca1, col.var = "cos2",
             gradient.cols = c("#FFCC00", "#CC9933", "#660033", "#330033"),
             repel = TRUE) +
  labs(title = "PCA of parameters", x="PC1 (83.3%)", y="PC2 (6.8%)",
       colour = "Treatments")+
  ggsave("PCA.png",  units="in", width=6.5, height=5.5) 
