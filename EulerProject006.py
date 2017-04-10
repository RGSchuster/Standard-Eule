#Here is brute force method for solving
seperate = []
together = 0
for i in range(1,11):
    seperate.append(i**2)
    together+=i
    i+=1
print((together**2)-sum(seperate))
#Here is formula method for solving
a = (100*(100+1)*(2*100+1))//6
b = 100*(100+1)//2
print(b**2 - a)
