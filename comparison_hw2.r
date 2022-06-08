# import needed libraries and csv file
library(ggplot2)
library(dplyr)
p_data <- read.csv(file = '/Users/tianencheng/Desktop/DATA.csv')
print(p_data)

# revision data
Divident <- function(prb){p_data$time[p_data$problem == prb & p_data$language == "C"]}
D_Size <- function(prb){p_data$size[p_data$problem == prb & p_data$language == "C"]}
p_data$lc <- ifelse(p_data$language %in% c("C"), "line", "point")
p_data$reltime <- p_data$time/Divident(p_data$problem)
p_data$relsize <- p_data$size/D_Size(p_data$problem)
print(p_data) # data after revision

# plotting
ggplot(data = p_data, aes(x = problem, y =reltime,col =  language, shape = language)) +
  geom_point(data = filter(p_data, p_data$lc !="line"), size = 3,)+
  geom_line(data=filter(p_data, p_data$lc == "line"), aes(x=problem, y=reltime, group=language))+
  scale_y_log10(breaks = 10^(0:3))

ggplot(data = p_data, aes(x = problem, y =relsize,col =  language, shape = language)) +
  geom_point(data = filter(p_data, p_data$lc !="line"), size = 3,)+
  geom_line(data=filter(p_data, p_data$lc == "line"), aes(x=problem, y=reltime, group=language))


