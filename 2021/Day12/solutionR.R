# Day 12 - paths!

rm(list = ls())

setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day12')
library(tidyverse)


data <- read_tsv(file = "input.txt", col_names = FALSE) %>% 
  separate(col = X1, into = c("Start","End"), sep="-")

# Finding list of all nodes 
allnodes <- pivot_longer(data, cols =  c("Start","End"), names_to = "node") %>% 
  select(value) %>% 
  distinct()