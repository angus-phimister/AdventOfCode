# Day 6 
# Crabs!


rm(list = ls())

##
library(tidyverse)
setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day7')

# Positions
starting <- read_csv(file = "input.txt", col_names = FALSE) %>% 
  pivot_longer(cols = everything(), names_to = "fish") %>% 
  select(value)

# Mean
mn<-summary(starting$value)[[3]] %>% 
  round()

fuelUse <- starting %>% 
  mutate(diff = abs(value-mn))%>% 
  summarize(tchange = sum(diff))
fuelUse




 
## Brute forcing it 
starting_vector <- starting %>% 
  pull(value)



min = min(starting_vector)
max = max(starting_vector)

distances <- rep(0,length(min:max)-1)

for (i in min:max) {
  
  distances[i] = sum(abs(starting_vector - i))
  
}

min(distances)

# Part B 
distance2 <- function(a, b) {
  intdiff = abs(a - b) 
  distance=(intdiff*(intdiff +1))*0.5
  return(distance)
}

distances2 <- rep(0,length(min:max)-1)
for (i in min:max) {
  distances2[i] = sum(distance2(starting_vector,i))
}
min(distances2)






