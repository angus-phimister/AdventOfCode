


## Advent Code Calender
# Day 4
# Bingo!

rm(list = ls())
setwd('/Users/adamhendry/Documents/Day 4 - R Coding')

# Numbers generated in this order
numbers <- c(31,50,68,16,25,15,28,80,41,8,75,45,96,9,3,98,83,27,62,42,59,99,95,13,55,10,23,84,18,76,87,56,88,66,1,58,92,89,19,54,85,74,39,93,77,26,30,52,69,48,91,73,72,38,64,53,32,51,6,29,17,90,34,61,70,4,7,57,44,97,82,37,43,14,81,65,11,22,5,36,71,35,78,12,0,94,47,49,33,79,63,86,40,21,24,46,20,2,67,60)

library(tidyverse)

# Naming the columns
cols = c("X1","X2","X3","X4","X5")
# Load List of Games 
games <- read_csv(file = "bing boards.csv", col_names = FALSE, trim_ws = TRUE) %>% 
  # Tidying data by getting rid of blank cells
  select(X1) %>% 
  drop_na() %>% 
  # Stripping out the spaces so that number align in rows and columns
mutate(X1 = str_replace_all(X1, " ", " ")) %>% 
  mutate(X1 = str_replace_all(X1, "  ", " "))
gamesMatrix <-  separate(games, col = X1, into = cols, sep = " ", remove = FALSE)

gamesList <- list() 

x = 1 
# Grouping the boards 1-5 6-11 and so on
for (i in seq(from=5, to=500, by=5)) {
  y = i-4
  print(gamesMatrix[y:i,1:5])
  gamesList[[x]]<-gamesMatrix[y:i,1:5]
  x = x+1
}

# Creating the vectors for the scores and counts (e.g.number of bingo calls made before board wins)
scores<-rep(0,100)
counts<-rep(0,100)

for(board in 1:100){

    testMatrix <- as.matrix(gamesList[[board]])
    solutionMatrix <- matrix(rep(0,25), nrow  = 5, ncol = 5)
    
    count<-0
    for (num in numbers) {
      count=count+1
      ans<- testMatrix %in% num
      solutionMatrix[ans]=1
      
    # Checking if board has won
      rows<- rowSums((solutionMatrix))
      cols<- colSums((solutionMatrix))
      
    maxrow<- max(rows)
    maxcol<- max(cols)
    
    if(maxrow==5 | maxcol==5){
      scoreIndex<-solutionMatrix==0
      scoreNumbers<-as.numeric(testMatrix[scoreIndex])
      score=sum(scoreNumbers)*num
      print(score)
      counts[board]=count
      scores[board]=score
      print("gameover")
      break
    }
    
    }
}

winningGame<-which.min(counts)
scores[winningGame]
  
# Solving part 2 of the problem
losingGame<-which.max(counts)
scores[losingGame]
