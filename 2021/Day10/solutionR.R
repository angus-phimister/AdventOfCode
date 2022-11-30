# Day 10 - Syntax errors! 

rm(list = ls())

setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day10')
library(tidyverse)

string <-"{([(<{}[<>[]}>{[]{[(<()>"
data <- read_tsv(file = "input.txt", col_names = FALSE) %>% as.matrix()

 #  "1 - {}","2 - []","3 - <>","4 - ()"
  opening <- c("{","[","<","(")
  closing <- c("}","]",">",")")
  
findCorrupt <- function(string) {

  length <- str_length(string)
  string_sep <- str_split(string, pattern ="") %>% unlist()
  
  # opening bracket 
  last_open <- string_sep[1]
  
  if (last_open %in% closing) {
    return(last_open)
  }
  
  
  for (i in 2:length) {
    
    bracket <- string_sep[i]
    # print(bracket)
    # If opening bracket, save 
    if (bracket %in% opening) {
      last_open <- c(last_open, bracket)
      # print(last_open)
    }
    # If closing bracket, must match the last opening bracket 
    if (bracket %in% closing) {
      equiv_opening = opening[closing %in% bracket]
      # print("Equiv opening")
      # print(equiv_opening)
      # print("Opening in string")
      # print(last_open[length(last_open)])
      if (last_open[length(last_open)] == equiv_opening) {
        last_open <- last_open[1:(length(last_open)-1)] # get rid of the last one
      } else {
        # Here they didnt match last opening bracket
        return(bracket)
      }
      
    }
  }    
  return(NA)  
}
  
  

corruptLines <- lapply(data, findCorrupt) %>% unlist() 
ans <- corruptLines[!is.na(corruptLines)] %>% 
  as_tibble()  %>% 
  mutate(score = case_when(
    value ==")" ~ 3,
    value == "]" ~ 57,
    value == "}" ~ 1197,
    value == ">" ~ 25137
  )) %>% 
  summarize(total = sum(score))
ans[1,1]


# Part 2 
data2 <-data[is.na(corruptLines)] %>% as.matrix()
string <- "[({(<(())[]>[[{[]{<()<>>"
completeLine <- function(string) {
  
  length <- str_length(string)
  string_sep <- str_split(string, pattern ="") %>% unlist()
  
  # opening bracket 
  last_open <- string_sep[1]

  for (i in 2:length) {
    
    bracket <- string_sep[i]
    # If opening bracket, save 
    if (bracket %in% opening) {
      last_open <- c(last_open, bracket)
      # print(last_open)
    }
    # If closing bracket, must match the last opening bracket 
    if (bracket %in% closing) {
      equiv_opening = opening[closing %in% bracket]

      if (last_open[length(last_open)] == equiv_opening) {
        last_open <- last_open[1:(length(last_open)-1)] # get rid of the last one
      } 
    }
  }    
  
  # Now loop from the end of the remaining opening brackets 
  
  complete <- ''
  for (k in length(last_open):1) {
    bracket <- last_open[k]
    equiv_closing  = closing[opening %in% bracket]
    complete <- c(complete, equiv_closing)
  }
  complete <- complete[2:length(complete)]
  # return(complete)
  
  score <- 0 
  for (j in 1:length(complete)) {
    score <- score*5 
    
    if (complete[j] == ")") {
      score <- score + 1
    } else if (complete[j] == "]") {
      score  <- score + 2 
    } else if (complete[j] == "}") {
      score <- score + 3
    } else {
      score <- score + 4 
    }
  }
  return(score)
}

scores <-lapply(data2,completeLine) %>%  unlist() %>% as_tibble()

medianScore <-scores %>% 
  summarise(mean = median(value))
medianScore[1,1]



  
  
  