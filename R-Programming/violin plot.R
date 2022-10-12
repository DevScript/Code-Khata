# Violin plot in ggplot
#geom_voilen()

install.packages('ggplot2')
library(ggplot2)

data("diamonds")

d_sample <- diamonds[seq(1,53000,by=100),]
nrow(d_sample)

p <- ggplot(d_sample, aes(cut,price,color=cut))+geom_violin()

p

p+geom_boxplot(width=0.1)+geom_jitter(size=0.5)+ggsave("violinplot.pdf")
