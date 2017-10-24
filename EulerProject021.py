import math
PropDivSum = 0
#This method compiles a list of proper divisors, sums them, then returns the sum
def PropDiv (n):
    divisors = [1] #by starting with 1, the list doesn't add n to it
    for i in range(2,math.floor(math.sqrt(n))+1): #check divison of numbers 2 thru sqrt(n)
        if n%i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(n//i)
    return sum(divisors) #using built in sum feature to add all values in list
#The main program calculates all the amicable numbers below 10,000.
#This doesn't count numbers that have divisors summing to themselves (ie. 28)
for j in range(1,10000):
    holder=PropDiv(j)
    if holder != 1: #no reason to check prime numbers
        if (holder!=j) & (j == PropDiv(holder)):
            PropDivSum += j

print(PropDivSum)
