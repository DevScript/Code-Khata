install.packages("ggthemes")
install.packages("multcompView")
install.packages("dplyr")

library(ggplot2)
library(ggthemes)
library(multcompView)
library(dplyr)

#Bar plots ---------


library(readxl)
For_Bar_Plots <- read_excel("BaBaG/For Bar Plots.xlsx", 
                            range = "A1:F5")
View(For_Bar_Plots)

p <- ggplot(For_Bar_Plots, aes(x = Names, y = Mean)) +
  geom_bar(stat = "identity", aes(fill = Names), show.legend = FALSE, width = 0.6) + #barplot
  geom_errorbar( #this argument is putting sd as error bars
    aes(ymin = Mean-SE, ymax=Mean+SE), 
    width = 0.1
  ) + 
  scale_fill_brewer(palette = "BrBG", direction = 1) + #theme setting
  ggthemes::theme_par(); p


For_Bar_Plots1 <- read_excel("BaBaG/For Bar Plots.xlsx", 
                            sheet = "2", range = "A1:F8")
View(For_Bar_Plots1)

p <- ggplot(For_Bar_Plots1, aes(x = Names, y = Mean)) +
  geom_bar(stat = "identity", aes(fill = Names), show.legend = FALSE, width = 0.6) + #barplot
  geom_errorbar( #this argument is putting sd as error bars
    aes(ymin = Mean-SE, ymax=Mean+SE), 
    width = 0.1
  ) + 
  scale_fill_brewer(palette = "BrBG", direction = 1) + #theme setting
  ggthemes::theme_par(); p


For_Bar_Plots2 <- read_excel("BaBaG/For Bar Plots.xlsx", 
                            sheet = "3")
View(For_Bar_Plots2)

p <- ggplot(For_Bar_Plots2, aes(x = Names, y = Mean)) +
  geom_bar(stat = "identity", aes(fill = Names), show.legend = FALSE, width = 0.6) + #barplot
  geom_errorbar( #this argument is putting sd as error bars
    aes(ymin = Mean-SE, ymax=Mean+SE), 
    width = 0.1
  ) + 
  scale_fill_brewer(palette = "BrBG", direction = 1) + #theme setting
  ggthemes::theme_par(); p


For_Bar_Plots3 <- read_excel("BaBaG/For Bar Plots.xlsx", 
                            sheet = "4")
View(For_Bar_Plots3)

p <- ggplot(For_Bar_Plots3, aes(x = Names, y = Mean)) +
  geom_bar(stat = "identity", aes(fill = Names), show.legend = FALSE, width = 0.6) + #barplot
  geom_errorbar( #this argument is putting sd as error bars
    aes(ymin = Mean-SE, ymax=Mean+SE), 
    width = 0.1
  ) + 
  scale_fill_brewer(palette = "BrBG", direction = 1) + #theme setting
  ggthemes::theme_par(); p

For_Bar_Plots4 <- read_excel("BaBaG/For Bar Plots.xlsx", 
                             sheet = "5")
View(For_Bar_Plots4)

p <- ggplot(For_Bar_Plots4, aes(x = Names, y = mean)) +
  geom_bar(stat = "identity", aes(fill = Names), show.legend = FALSE, width = 0.6) + #barplot
  geom_errorbar( #this argument is putting sd as error bars
    aes(ymin = mean-SE, ymax=mean+SE), 
    width = 0.1
  ) + 
  scale_fill_brewer(palette = "BrBG", direction = 1) + #theme setting
  ggthemes::theme_par(); p



# Scatter plot-----

scatter_plot <- read_excel("BaBaG/scatter plot.xlsx", 
                           sheet = "1")
View(scatter_plot)

plot(x=scatter_plot$X,y=scatter_plot$Y)

scatter_plot1 <- read_excel("BaBaG/scatter plot.xlsx", 
                           sheet = "2")
View(scatter_plot1)

plot(x=scatter_plot1$X1,y=scatter_plot1$Y1)

plot(x=scatter_plot1$X2,y=scatter_plot1$Y2)

scatter_plot2 <- read_excel("BaBaG/scatter plot.xlsx", 
                            sheet = "3")
View(scatter_plot2)

plot(x=scatter_plot2$X,y=scatter_plot2$Y)


scatter_plot3 <- read_excel("BaBaG/scatter plot.xlsx", 
                            sheet = "4")
View(scatter_plot3)

plot(x=scatter_plot3$X,y=scatter_plot3$Y)


scatter_plot4 <- read_excel("BaBaG/scatter plot.xlsx", 
                            sheet = "5")
View(scatter_plot4)

plot(x=scatter_plot4$X,y=scatter_plot4$Y)
