## Advent Code Calender
# Day 2

# Finding the number of increases 

rm(list = ls())


# Load data
library(tidyverse)
setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day2')
data <- read_tsv(file = 'input.txt', col_names = FALSE)


data <- data %>% 
  separate(col = X1, into = c("direction", "magnitude"), sep = " ", remove = TRUE) %>% 
  mutate( magnitude = as.double(magnitude))
# Clean Data
df1 <- data %>% 
  mutate(
    x_move = case_when(
    direction == "forward"   ~ magnitude,
    TRUE  ~ 0
          ), 
    y_move = case_when(
      direction== "down"   ~ magnitude,
      direction== "up" ~ -1*magnitude,
    TRUE  ~ 0
     )) %>% 
  summarize(total_x = sum(x_move, na.rm = TRUE),
            total_y = sum(y_move, na.rm = TRUE)) %>% 
  mutate(t = total_y*total_x)



df2 <-  data %>% 
  mutate(
    
  ## Calculating Aim
    aim_change = case_when(
      direction== "down"   ~ magnitude,
      direction== "up" ~ -magnitude,
      TRUE ~ 0 
    ),
    aim_cumsum= cumsum(aim_change),
    
    
  ## Calculating x change
  x_move = case_when(
    direction == "forward"   ~ magnitude,
    TRUE  ~ 0
  ),

  ## Depth move 
  y_move = case_when(
    direction== "forward"   ~ magnitude*aim_cumsum,
    TRUE  ~ 0
  )
 ) %>% 
  summarize(total_x = sum(x_move, na.rm = TRUE),
            total_y = sum(y_move, na.rm = TRUE)) %>% 
  mutate(t = total_y*total_x)


