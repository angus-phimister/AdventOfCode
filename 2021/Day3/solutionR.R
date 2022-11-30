# Day 3

# Finding most common digit 
rm(list = ls())

base2decimal = function(base_number, base = 2) {
  split_base = strsplit(as.character(base_number), split = "")
  return(sapply(split_base, function(x) sum(as.numeric(x) * base^(rev(seq_along(x) - 1)))))
}


library(base)
library(tidyverse)
setwd('C:/Users/angus/Documents/GitHub/AdventOfCode2021/Day3')
rawdata <- read_tsv(file = 'input.txt', col_names = FALSE)

cols <- sprintf("X%s",seq(1:13))

data <- rawdata %>% 
  separate(col = X1, into = cols, sep = "", remove = TRUE) %>% 
  select(X2:X13) %>% 
  mutate_all(as.numeric) %>% 
  summarise(across(where(is.numeric), ~ sum(.x, na.rm = TRUE)))

gamma<-data %>% 
  mutate(across(where(is.numeric), ~ if_else(.x>500,1,0))) %>% 
  mutate_all(as.character) %>% 
  unite(col = gamma,everything() , sep="") %>% 
  mutate_all(as.numeric) %>% 
  mutate(numGamma = base2decimal(gamma))
  
beta <- data %>% 
  mutate(across(where(is.numeric), ~ if_else(.x<500,1,0))) %>% 
  mutate_all(as.character) %>% 
  unite(col = beta,everything() , sep="") %>% 
  mutate_all(as.numeric) %>% 
  mutate(numBeta = base2decimal(beta))

answer <- gamma$numGamma * beta$numBeta
print(answer)

## Question 2
data <- rawdata %>% 
  separate(col = X1, into = cols, sep = "", remove = TRUE) %>% 
  select(X2:X13) %>% 
  mutate_all(as.numeric)


dataLoop <- data
for (i in 1:12) {
  nObs <- as.double(count(dataLoop))
  threshold <- nObs/2
  
  sumAnswer <- as.double(summarize(dataLoop, mn = sum(dataLoop[i])))
  print(threshold)
  print(sumAnswer)
    if (sumAnswer>=threshold) {
      dataLoop <- filter(dataLoop, dataLoop[i]==1)
    }
    else {
      dataLoop <- filter(dataLoop, dataLoop[i]==0)
    }
}


oxgen <- dataLoop %>% 
  mutate_all(as.character) %>% 
  unite(col = oxgen,everything() , sep="") %>% 
  mutate_all(as.numeric) %>% 
  mutate(numOx = base2decimal(oxgen))


dataLoop <- data
for (i in 1:12) {
  nObs <- as.double(count(dataLoop))
  threshold <- nObs/2
  
  sumAnswer <- as.double(summarize(dataLoop, mn = sum(dataLoop[i])))
  print(threshold)
  print(sumAnswer)
  
  if (nObs==1) {
    break
  }
  
  if (sumAnswer>=threshold) {
    dataLoop <- filter(dataLoop, dataLoop[i]==0)
    print("Chosen number is 0")
  }
  else {
    dataLoop <- filter(dataLoop, dataLoop[i]==1)
    print("Chosen number is 1")
  }
}


co2  <- dataLoop %>% 
  mutate_all(as.character) %>% 
  unite(col  = co2,everything() , sep="") %>% 
  mutate_all(as.numeric) %>% 
  mutate(numCO2  = base2decimal(co2))

answer <- co2$numCO2 * oxgen$numOx
print(answer)

