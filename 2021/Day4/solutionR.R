## Advent Code Calender
# Day 3

# Bingo!

rm(list = ls())

setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day4')

library(tidyverse)

# Load list of numbers 
number <- as.matrix(read_csv(file = "input1.txt", col_names = FALSE))
  
# Load List of Games 
cols = c("X1","X2","X3","X4","X5")
games <- read_tsv(file = "bingoboards.txt", col_names = FALSE, trim_ws = TRUE) %>% 
  mutate(X1 = str_replace_all(X1, " ", " ")) %>% 
  mutate(X1 = str_replace_all(X1, "  ", " "))

gamesMatrix <-  separate(games, col = X1, into = cols, sep = " ", remove = FALSE) %>% 
          mutate_if(is.character, as.numeric)


gamesList <- list() 

x = 1 
for (i in seq(from=5, to=500, by=5)) {
  print(i)
  y = i-4
  print(gamesMatrix[y:i,])
  gamesList[[x]]<-gamesMatrix[y:i,]
  x = x+1
}


testMatrix <- gamesList[[1]]
solutionMatrix <- matrix(rep(FALSE,25), nrow  = 5, ncol = 5)
for (num in 1:5) {
  ans<- testMatrix %in% num
  solutionMatrix = ans | 
}





