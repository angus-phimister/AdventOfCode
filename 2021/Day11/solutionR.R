# Day 11 - Octopusus!

rm(list = ls())

setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day11')
library(tidyverse)

names <- c("x1","x2","x3","x4","x5","x6","x7","x8","x9","x10","x11")
data <- read_tsv(file = "input.txt", col_names = FALSE) %>%
  as_tibble() %>% 
  separate(col = X1, into = names, sep = "") %>% 
  mutate_if(is.character, as.numeric) %>% 
  select(x2:x11) %>% 
  as.matrix()


neighbours <- function(i,j, matrix) {
  
  bound <- dim(matrix)
  
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
    neighbours <- list(c(i+1,j), c(i, j+1), c(i+1,j+1))
  } else if (cornerUR) {
    neighbours <- list(c(i+1,j), c(i, j-1), c(i+1,j-1))
  } else if (cornerLL) {
    neighbours <- list(c(i-1,j), c(i, j+1), c(i-1,j+1))
  } else if (cornerLR) {
    neighbours <- list(c(i-1,j), c(i, j-1), c(i-1,j-1))
  } else if (sideTop) {
    neighbours <- list(c(i+1,j), c(i, j-1), c(i, j+1), c(i+1,j-1), c(i+1,j+1))
  } else if (sideLeft) {
    neighbours <- list(c(i+1,j), c(i-1, j), c(i, j+1), c(i+1,j+1), c(i-1,j+1))
  } else if (sideRight) {
    neighbours <- list(c(i-1,j), c(i, j-1), c(i+1, j), c(i+1,j-1), c(i-1,j-1))
  } else if (sideBottom) {
    neighbours <- list(c(i-1,j), c(i, j-1), c(i, j+1), c(i-1,j+1), c(i-1,j-1))
  } else {
    neighbours <- list(c(i+1,j), c(i-1, j), c(i,j-1), c(i, j+1),
                       c(i+1,j+1), c(i-1, j+1), c(i+1,j-1), c(i-1, j-1))
  }
  
  return(neighbours)
  
}


updatedMatrix <- function(matrix) {
# Step 1 - increment whole matrix by 1  

updated <- matrix + 1

# Find indexes of those who flast 
updatedFlashS1 <- which(updated > 9, arr.ind = TRUE)

# check if none updated after step 1, end
if (dim(updatedFlashS1)[1] == 0) {
  count = 0 
  return(list(updated,count))
}

exit_flag = FALSE
while (exit_flag == FALSE) {  
# replace 9's with NA's (to stop them flashing again)
  updated[updated>9] <- NA
  
  dimFS1 <- dim(updatedFlashS1)[1]
    
    # For each index which hits 9, go through and add 1 to all neighbours
    for (i in 1:dimFS1) {
      # print(i)
      # find the list of neighbours
      nlist <- neighbours(updatedFlashS1[i,][1],updatedFlashS1[i,][2], updated)
      
      # for each neighbour add one 
      for (j in 1:length(nlist)) {
      #  print(j)
        updated[nlist[[j]][1],nlist[[j]][2]] <- updated[nlist[[j]][1],nlist[[j]][2]]  + 1 
      }
    
    }

# Check if anyone has hit the threshold
# Find the ind
updatedFlashS2 <- which(updated > 9, arr.ind = TRUE)

# # Update the matrix to NA's if anyone is above 9
# updated[updated>=9] <- NA

if (dim(updatedFlashS2)[1] == 0 ){
  exit_flag = TRUE
}
# New flashes save as 1, and repeat loop
updatedFlashS1 <- updatedFlashS2 
}

# Replace NA's with 0 
# matrix <- updated
count <- sum(is.na(updated))
updated[is.na(updated)] = 0

return(list(updated,count))
}  


matrix = data 
print(matrix)
count = 0 
for (i in 1:100) {
  ans <- updatedMatrix(matrix)
  matrix <- unlist(ans[1]) %>% 
    matrix(ncol=10)
  print(matrix)
  count = count + unlist(ans[2])
}

# Part 2 
matrix = data 
nflash = 0 
x = 0
while (nflash!= 100) {
  ans <- updatedMatrix(matrix)
  matrix <- unlist(ans[1]) %>% 
    matrix(ncol=10)
  nflash <- unlist(ans[2])
  x = x + 1 
  print(x)
}






#illegal_score <- c(')' = 3, ']' = 57, '}' = 1197, '>' = 25137)



