#All numbers must start and end with 3,5, or 7
#First I want to look at two digit primes ending or starting with 3,5,7

#make a prime list
primes = [2]
i = 3
while i<1000:
    for j in range(len(primes)):
        if (i%primes[j] == 0):
            break
        if j==len(primes)-1:
            primes.append(i)
    i += 2 #only check odd numbers

#Starting: 31, 37, 53, 59, 71, 73, 79
#Ending: 13, 17, 23, 47, 43, 47, 53, 73, 83, 97

#This checks for 3,5 or 7
def isDigitOfInterest(num):
    return {3 : True, 5 : True, 7 : True}.get(num)

cleanPrimes = []
for i in range(len(primes)):
    if primes[i] < 10:
        continue
    temp = primes[i]
    if isDigitOfInterest(temp%10) and isDigitOfInterest(int(str(temp)[0])):
        cleanPrimes.append(temp)
    if primes[i] >= 100:
        break
    
print(cleanPrimes)
