# scatter plot

library(ggplot2)

data("cars")
View(cars)

ggplot(data=cars,aes(x=speed,y=dist))+geom_point()+
  geom_smooth()

ggplot(data=cars,aes(x=speed,y=dist))+geom_point()+
  geom_smooth(method='lm',se=F,level=0.05)


# scatter plot with multiline

data("Orange")
View(Orange)
ggplot(Orange, aes(age,circumference,color=Tree))+geom_point(size=4,shape=16)

# Serperate by shape

ggplot(Orange, aes(age,circumference,color=Tree))+geom_point(size=4,shape=19)+geom_line(linetype=2,size=1)+labs(x="Age",y="Circumference",title="Graph")

                                                             
ggsave("scatterplot.pdf")



# Buble plot
install.packages("viridis")
library(viridis)
data("quakes")S
nrow(quakes)
q_sample <- quakes[seq(from=1,to=1000,by=10),]
nrow(q_sample)

ggplot(data=q_sample,aes(x=lat,y=long))+geom_point(aes(size=mag,color=mag))+guides(size=F)+scale_color_viridis_b(option="B")+scale_size_continuous(range=c(1,9))+labs(x="Latitude",y="Longitude",title="Graph")
ggsave("bubleplot.pdf")

#jitter plot
#data()
data("diamonds")
nrow(diamonds)
d_sample <- diamonds[seq(from=1,to=49000,by=10),]
nrow(d_sample)

ggplot(d_sample,aes(cut, price))+geom_point()
ggplot(d_sample,aes(cut, price))+geom_jitter() #good

ggplot(d_sample,aes(cut, price,color=cut))+geom_jitter()

# moer plot so use jitter
