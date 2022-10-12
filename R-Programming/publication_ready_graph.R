install.packages("ggthemes")
install.packages("multcompView")
install.packages("dplyr")

library(ggplot2)
library(ggthemes)
library(multcompView)
library(dplyr)


data('chickwts')
tibble(chickwts)

mean_data <- group_by(chickwts, feed) %>% #feed is our treatmnet in this example
  summarise(weight_mean=mean(weight), sd = sd(weight)) %>% #to calculate mean and SD
  arrange(desc(weight_mean)) #to arange in descending order
tibble(mean_data)

anova <- aov(weight ~ feed, data = chickwts)
summary(anova)

tukey <- TukeyHSD(anova)
tukey

group_letters <- multcompLetters4(anova, tukey)
# we have to mention both anova model and tukey objects to get group letters
group_letters

p <- ggplot(mean_data, aes(x = feed, y = weight_mean)) +
  geom_bar(stat = "identity", aes(fill = feed), show.legend = FALSE, width = 0.6) + #barplot
  geom_errorbar( #this argument is putting sd as error bars
    aes(ymin = weight_mean-sd, ymax=weight_mean+sd), 
    width = 0.1
  ) + 
  geom_text(aes(label = group_letters, y = weight_mean + sd), vjust=-0.4) + #add letters
  scale_fill_brewer(palette = "BrBG", direction = 1) + #theme setting
  labs(#this will add labels 
    x = "Feed Type",
    y = "Chicken Weight (g)",
    title = "Publication Ready Barplot",
    subtitle = "Made by #RwithAammar",
    fill = "Feed Type"
  ) +
  ylim(0,410)+ #change your yaxis limits based on the letters
  ggthemes::theme_par(); p

tiff('Barplot.tiff', units="in", width=10, height=6, res=300, compression = 'lzw')
p
dev.off()