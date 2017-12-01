#I am going to copy the divisors function from problem 21.
#I will then use it to build a list of abundant numbers
#I could solve this by then building a list of all sums of abundant numbers
#or checking a for loop from 1-28123 and adding to a new list all numbers that
#cannot be written as the sum of two abundant numbers.
#This method seems very memory hungry as it is 3 or 4 nested loops.

import math

abundNums = []

def PropDiv (n):
    #by starting with 1, the list doesn't add n to it
    divisors = [1]
    #check divison of numbers 2 thru sqrt(n)
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(n//i)
    return sum(divisors)

#This checks if a number is abundant, starts at 12 b/c smallest abund. num
for i in range(12,28124):
    if PropDiv(i) > i:
        abundNums.append(i)

#At this point, I can make a list of any range of abundant numbers.
#Now I want to make nested loops that check if a number is the sum of two numbers on that list.

##i = 24
##j = 0
##k = 0
##done = 'false'
count = 0

#for loop to fill numbers with 1-23
for holder in range(1,24):
    count += holder

##while i < 28124:
##    while abundNums[j] < i:
##        while abundNums[k] < i:
##            if ((i - abundNums[j]) == abundNums[k]):
##                done = 'true'
##                break
##            elif (abundNums[j] + abundNums[k] > i) & (abundNums[j] > abundNums[k]):
####                print(abundNums[j],abundNums[k],i)
##                count += i
##                done = 'true'
##                break
##            elif (abundNums[j] + abundNums[k] > i):
##                break
####            print(abundNums[j],abundNums[k])
##            k += 1
##        j += 1
####        print()
##        k = 0
##        if done == 'true':
##            break
##    i += 1
##    j = 0
##    done = 'false'
    
#This has not compiled in several minutes. Time for a new plan.
#New idea is to compile a list of all sums of abundant numbers,
#then iterate through all numbers and count them unless they are in the list
#(or something more efficient)

numSums = []

for i in range(len(abundNums)):
    for j in range(i,len(abundNums)):
        numSums.append(abundNums[i]+abundNums[j])

#Learning about sets in Python. I can make a set of all numbers 1-28123
#and then subtract the set of numbers that are a sum of abund nums

notSums = list(set(range(1,28123)) - set(numSums))

print('The answer is ' + str(sum(notSums)))

#I have decided to keep my old attempts in the code here.
#I know it is not clean, but it shows my thought processes and trials.
