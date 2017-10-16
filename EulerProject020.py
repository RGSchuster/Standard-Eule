#I am going to build an array of increasing factorials
#Memoization is faster here than re-calculating each multiple up to 100
factorials = [1]
summation = 0
for i in range(2,100):
    factorials.append(i*factorials[i-2])

for digits in str(factorials[len(factorials)-1]):
    summation += int(digits)

print(summation)
