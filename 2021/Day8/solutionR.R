# Day 8 - Part 1 
# Decoding 


rm(list = ls())

##
library(tidyverse)
setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day8')

x = c("x1", "x2","x3", "x4","x5", "x6","x7", "x8","x9", "x10","x11", "x12","x13", "x14", "x15")

raw <- read_tsv(file = "input.txt", col_names = FALSE) %>% 
  separate(col = X1, into =x, sep = " ")


output <- select(raw, x12:x15)
signal <- select(raw, x1:x10)
rm(raw)



# Part 1 

# 1 (2 segments) ; 4 (4 segments) ; 7 (3 segments) ; 8 (7 segments)
tlengths <- c(2,4,3,7)
# Count of 2 digit length 
outputCount <- output %>% 
  mutate(across(.cols = everything(),  ~ str_length(.x)))

outputCountInd<-  mutate(outputCount, across(.cols = everything(), ~ if_else(.x %in% tlengths,1,0))) %>% 
  mutate(sumRow = rowSums(across(everything()))) %>% 
  summarize(count = sum(sumRow))
