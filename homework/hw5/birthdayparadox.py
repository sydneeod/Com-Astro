import random as rand

## initialization
npeople = 23 ## number of people 
ntrials = 1000 ## number of trials 

def birthday_array(npeople): ## function used to generate an array of 23 random birthdays
    birthdays = []
    
    for i in range(npeople): ## loop through people and assign random birthday
        birthdays.append(rand.randint(1,365)) ## random birthdays 1 through 365
        
    return birthdays

def matches(birthdays):
    non_rep_birthdays = set(birthdays) ## this gives a list of all the non repeating birthdays
    totalBdays = npeople 
    bdayCount = len(non_rep_birthdays) ## number of nonrepeating birthdays
    repeatingBdays = (totalBdays != bdayCount) ## return true or false depending, is passed into probability function to add to the count
    
    return repeatingBdays

def probability():
    
    count = 0 ## initializing my counter
    
    for i in range(ntrials): ## loop through trials 
        birthdays = birthday_array(npeople) ## grab birthday arrays
        repeatingBdays = matches(birthdays) ## find if any birthdays repeat
        
        if repeatingBdays: ## add to count if bdays repeat 
            count += 1

    prob = (count/ntrials)*100 ## final probability 
    
    return prob

prob = probability()

print(f"Estimated probability for matching birthdays for {npeople} is {prob}%")
