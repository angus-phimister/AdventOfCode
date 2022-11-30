# Day 8 - Part 2 
# Mininimzing  

rm(list = ls())
setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day9')

library(tidyverse)
data <- read_tsv(file = "input.txt", col_names = FALSE) %>% 
  seperate(col = X1, into)



data <- scan(file = "input.txt", what = character()) %>% 
  strsplit(split = "") %>% 
  unlist()

dataMat<- matrix(as.double(data), ncol = 100, byrow=  TRUE )


# Minimum if lower than all the things around it 

findMinumum <- function(matrix) {
  
  # Find Boundaries 
  bound <- dim(matrix)
  minpos <- matrix(rep(FALSE,bound[1]*bound[2]), ncol = bound[1])
  
  
  for (i in 1:bound[1]) {
    for (j in 1:bound[2]) {
      
      # Corners
      cornerUL = (i == 1 & j == 1) 
      cornerUR = (i == 1 & j == bound[2]) 
      cornerLL = (i == bound[1] & j == 1) 
      cornerLR  =(i == bound[1] & j == bound[2])
      
      if (cornerUL) {
        minpos[i,j] = (matrix[i,j] < matrix[i,j+1])  & (matrix[i,j] < matrix[i+1,j])
        next
      }
      if (cornerUR) {
        minpos[i,j] = (matrix[i,j] < matrix[i+1,j]) & (matrix[i,j] < matrix[i,j-1])
        next
      }
      if (cornerLL) {
        minpos[i,j] = (matrix[i,j] < matrix[i,j+1]) & (matrix[i,j] < matrix[i-1,j])
        next
      }
      if (cornerLR) {
        minpos[i,j] = (matrix[i,j] < matrix[i,j-1]) & (matrix[i,j] < matrix[i-1,j])
        next
      }
      
      # Sides
      sideTop = (i == 1 ) 
      sideLeft = (j == 1) 
      sideRight = ( j == bound[2]) 
      sideBottom  =(i == bound[1] )
      
      if (sideTop) {
        minpos[i,j] = (matrix[i,j] < matrix[i,j+1]) & (matrix[i,j] < matrix[i+1,j]) & (matrix[i,j] < matrix[i,j-1])
        next
      }
      if (sideLeft) {
        minpos[i,j] = (matrix[i,j] < matrix[i,j+1]) & (matrix[i,j] < matrix[i-1,j]) & (matrix[i,j] < matrix[i+1,j])
        next
      }
      if (sideRight) {
        minpos[i,j] = (matrix[i,j] < matrix[i,j-1]) & (matrix[i,j] < matrix[i-1,j]) & (matrix[i,j] < matrix[i+1,j])
        next
      }
      if (sideBottom) {
        minpos[i,j] = (matrix[i,j] < matrix[i-1,j]) & (matrix[i,j] < matrix[i,j-1]) & (matrix[i,j] < matrix[i,j+1])
        next
      } 
      
      
      minpos[i,j] = (matrix[i,j] < matrix[i-1,j]) & (matrix[i,j] < matrix[i+1,j]) & (matrix[i,j] < matrix[i,j+1]) &  (matrix[i,j] < matrix[i,j-1])
      
    }
  }
  
  
 return(minpos) 
  
  
  
}


mins <- findMinumum(dataMat)
minList <- which(mins, arr.ind = TRUE)

whereMin <- sum(dataMat[mins]) + sum(mins)


# Part 2
edges <- ifelse(dataMat==9 ,1,0)
  

flowDown <- function(cell, matrix) {
  i = cell[1]
  j = cell[2]
  
  bound <- dim(matrix)

  
  value <- matrix[i,j]
  # print(value)
  # Dealing with 9's 
  if (value == 9) {
    return(c(NA,NA))
  }

  minv <- value
  exit_flag = FALSE
  x = 0 
  while (exit_flag == FALSE) {
   x = x + 1
   # print(i)
   # print(j)
   # print(c(i,j,minv))
   cmin <- c(i,j)
   
   # Corners 
   cornerUL = (i == 1 & j == 1) 
   cornerUR = (i == 1 & j == bound[2]) 
   cornerLL = (i == bound[1] & j == 1) 
   cornerLR  =(i == bound[1] & j == bound[2])
   # Sides
   sideTop = (i == 1 ) 
   sideLeft = (j == 1) 
   sideRight = ( j == bound[2]) 
   sideBottom = (i == bound[1])
   
   if (cornerUL) {
     neighbours <- list(c(i+1,j), c(i, j+1))
   } else if (cornerUR) {
     neighbours <- list(c(i+1,j), c(i, j-1))
   } else if (cornerLL) {
     neighbours <- list(c(i-1,j), c(i, j+1))
   } else if (cornerLR) {
     neighbours <- list(c(i-1,j), c(i, j-1))
   } else if (sideTop) {
     neighbours <- list(c(i+1,j), c(i, j-1), c(i, j+1))
   } else if (sideLeft) {
     neighbours <- list(c(i+1,j), c(i-1, j), c(i, j+1))
   } else if (sideRight) {
     neighbours <- list(c(i-1,j), c(i, j-1), c(i+1, j))
   } else if (sideBottom) {
     neighbours <- list(c(i-1,j), c(i, j-1), c(i, j+1))
    } else {
     neighbours <- list(c(i+1,j), c(i-1, j), c(i,j-1), c(i, j+1))
   }
  
 # print(neighbours) 
   
  for (k in 1:length(neighbours)) {
   nvalue <- matrix[neighbours[k][[1]][1], neighbours[k][[1]][[2]]]

        if (nvalue<=minv) {
         minv <- nvalue
         cmin <- c(neighbours[k][[1]])
       }
  }
  if (cmin[1] == i & cmin[2] == j ) {
     exit_flag = TRUE 
     break
  }  else {
    i = cmin[1] 
    j = cmin[2]
  }
   
 } 
 return(cmin)
}
  

x = 1
ans<-matrix(rep(c("",""),100*100), nrow = 100*100)
for (i in 1:100) {
  for (j in 1:100) {
    
    ans[x,] <- flowDown(c(i,j),dataMat) %>% as.character()
    
    x = x + 1
    
  }
}

ans2 <- ans %>% as_tibble()  %>%  mutate(v3 = paste(V1, V2, sep = ",")) %>% 
  filter(v3 != "NA,NA") %>%  select(v3) %>% 
  count(v3) %>% 
  slice_max(order_by = n, n = 3)




