#The naive solution would be to generate a list of all perms. then index 1,000,000
#But I can do this faster by 'narrowing' down each digit based on the index
#I need to remove each digit from a list so that I do not reuse them

import math

loc = 1000000

numsLeft = list(range(10))
finalNum = []
length = len(numsLeft)

while length > 0:
    
    #This loops identifies the section of the lexicographic based on the left-most unsolved digit
    #For example, all 10-digit numbers starting with a 0 will be the first through 362,879th number
    #The first number starting with a 1 will be the 362,880th number.
    #This means 1,000,000 falls in the 3rd section, between 725,760 and 1,088,640,
    #and thus begin with a 2.
    
    fullLoc = math.factorial(length) #number of combinations of digits still left
    index = math.floor((loc/fullLoc)*length) #"where" we are out of all possibilities
    finalNum.append(str(numsLeft[index])) #adds section's corresponding number to final
    loc = math.floor(((loc/fullLoc)*length)%1 * (fullLoc//length)) #finds new spot from where we left off
    numsLeft.remove(numsLeft[index]) #removes used number
    
    length = len(numsLeft)
    
print("".join(finalNum))


