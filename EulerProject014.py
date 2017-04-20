import math as mt

longestNum = 0
chainLength=1
longestChain = 0

for num in range(2,999999): #this checks every number <1million
    originalNum = num #keeps track of my number before calculations
    while True:
        if num==1: #when the loop is done, check if thats the longest chain
            if chainLength > longestChain:
                longestChain = chainLength
                longestNum = originalNum
            break
        elif num%2 == 0: #if number is even
            num = num//2
            chainLength += 1
        else: #else, ie. if number is odd. no need for elif here b/c nothing >2 is neither odd nor even
            num = (3*num + 1)
            chainLength += 1
    chainLength = 1 #reset chainLength
print(longestNum)
