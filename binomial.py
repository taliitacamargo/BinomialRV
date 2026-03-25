import numpy as np
import matplotlib.pyplot as plt 
from typing import List

def isPrime(n : int) -> bool: 
#create a value called divisor starting at 2
    divisor = 2
    while(divisor < n):
#if its divisible by n then its not prime
        if(n % divisor == 0):
            return 0
#otherwise we incremenet our divisor
        divisor += 1
    return 1
#You are still just doing a Bernouli RV instead of a binomial RV. 
# You should use nested loops - one to perform the number of random experiment simulations 
# (the outter loop) and one to actually run the random experiment (the inner loop). For the binomial RV,
#  you will keep track of the number of primes rolled during a single random experiment then append THAT value 
# to your outcomes.
def binomial(numSides : int, numSamples: int, numTrials : int) -> List:
    outcomes = []
# OUTER LOOP NEEDED
    for _ in range(numTrials):

        count = 0
# INNER LOOP
        for _ in range(numSamples):
#generate random num
            rand = np.random.randint(1, numSides + 1)
#determine whether or not this outcome is prime
            if(isPrime(rand)):
                count += 1
#if num is prime we APPEND THE RESULT 
        outcomes.append(count)
    return outcomes

if __name__ == "__main__":
# num of times rolled 
    numSamples = 21
# num of die sidec
    numSides = 2048
# Num of simulation iterations to run
    numTrials = 1000

    outcomes = binomial(numSides, numSamples, numTrials) 

#create a plot (figure out how to align it to the numbers :T)
    fig,ax = plt.subplots(num = 0, nrows = 1, ncols = 1, layout = "tight")
    ax.hist(x = outcomes,
# this sets the # of bins
            bins = range(0,23),
            edgecolor = "black",
            density = True,
            align="left",
# this sets the width of each bar on the graph 
            rwidth = 0.8)
    
    ax.set_title("Binomial Random Variables ", fontweight = 'bold')

    ax.set_xticks(range(0,22,2))
    ax.set_yticks(np.arange(0, 0.27, 0.02))
#grid look on graph
    ax.grid()

    ax.set_xlabel("Simulations", size = 10, fontweight = 'bold')
    ax.set_ylabel("Prime Rolls", size = 10, fontweight = 'bold')

    plt.show()
