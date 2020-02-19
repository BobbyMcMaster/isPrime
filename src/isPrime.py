#!/usr/bin/env python3

# obonhamcarter@allegheny.edu
# date 3 Sept 2019
# Bobby McMaster

data = open("../input/dataFile.txt")
numOfPrimes_int = 0
numOfNonPrimes_int = 0
numOfNums_int = 0


for line_str in data:
    #print( "line_str : ",line_str)
    numOfNums_int += 1
    try: # if the line contains something other than an integer
        n_int = int(line_str) # note: n_int is an integer
    except ValueError: # catch the non-integer
        pass

    isPrime = True

    # TO DO: Complete the program to check primality
    numLine = int(line_str)
    if numLine > 1:
        for i in range(2, numLine):
            if (numLine % i) == 0:
                numOfNonPrimes_int +=1
            break

numOfPrimes_int = numOfNums_int - numOfNonPrimes_int



print("    Number of values in file   : ",numOfNums_int)
print("    Number of primes           : ",numOfPrimes_int)
print("    Number of composites       : ",numOfNonPrimes_int)
