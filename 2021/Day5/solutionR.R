# Day 5
# Finding the lines


rm(list = ls())

# Load in the data

setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day5')
library(tidyverse)


coord1 <- c("x1","y1")
coord2 <- c("x2","y2")

rawdata <- read_tsv(file = "input.txt", col_names = FALSE) %>% 
  separate(col = X1, into = c("X1","X2"), sep="->") %>% 
  separate(col = X1, into = coord1, sep=",") %>% 
  separate(col = X2, into = coord2, sep=",") %>% 
  mutate_if(is.character, as.numeric)


# Finding the vertical and horizontal lines
dataPerp <- rawdata %>% 
  mutate(horizontal = if_else(x1==x2, 1, 0),
         vertical = if_else(y1==y2,1,0)) %>% 
  filter(vertical==1 | horizontal == 1) 

# Mins and max for matrix of lines
summary(rawdata) # matrix runs from 10 to 990


# Lines lines lines
len <- as.numeric(count(dataPerp))
lines <- matrix(data=rep(0,1000*1000), 1000,1000)


for (i in 1:len) {
  i1  = as.numeric(dataPerp[i,1])
  i2  = as.numeric(dataPerp[i,2])
  i3  = as.numeric(dataPerp[i,3])
  i4  = as.numeric(dataPerp[i,4])
  lines[i1:i3,i2:i4]  = lines[i1:i3,i2:i4] + 1
}

answer1 <- ifelse(lines>=2,1,0)
sum(answer1)

# Lines lines lines v2 
dataDiag <-rawdata %>% 
  mutate(horizontal = if_else(x1==x2, 1, 0),
         vertical = if_else(y1==y2,1,0)) 

len <- as.numeric(count(dataDiag))
lines <- matrix(data=rep(0,1000*1000), 1000,1000)


for (i in 1:len) {
  
  vertical = as.numeric(dataDiag[i,5])
  horizontal = as.numeric(dataDiag[i,6])
    
    i1  = as.numeric(dataDiag[i,1])
    i2  = as.numeric(dataDiag[i,2])
    i3  = as.numeric(dataDiag[i,3])
    i4  = as.numeric(dataDiag[i,4])  
    
  if (vertical == 1 | horizontal == 1) {
    lines[i1:i3,i2:i4]  = lines[i1:i3,i2:i4] + 1   
  }
  else {
     y = i2
     
     if (i2>i4) {
       sign = -1
     } 
     else {
       sign = 1
     }
     
    for (j in i1:i3) {
      lines[j,y] = lines[j,y] + 1 
      y = y + sign 
    }
    test = y == i4 
  }
}

answer2 <- ifelse(lines>=2,1,0)
sum(answer2)



