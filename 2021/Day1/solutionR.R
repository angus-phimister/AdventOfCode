## Advent Code Calender
# Day 1

# Findng the number of increases 

rm(list = ls())


# Load data
library(tidyverse)
setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day1')
data <- read_tsv(file = 'input.txt', col_names = FALSE)


data_increase1<- mutate(data, X1L = lag(X1),
              increase = if_else(X1>X1L,1,0))%>% 
  summarise(total = sum(increase, na.rm = TRUE))
data_increase1

data_increase2 <- data %>% 
  mutate(lag2 = lag(X1,n = 2),
         lag1 = lag(X1,n = 1),
        sum3 = X1+lag1+lag2,
        sumLag = lag(sum3 , n=1),
        increase = if_else(sum3>sumLag,1,0))
%>% 
  summarise(total = sum(increase, na.rm = TRUE))
data_increase2
