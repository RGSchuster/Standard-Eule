#taking prime list maker from Problem 7
pList = [2]
for i in range(3,2000000):
    for j in range(0,len(pList)):
        if (i%pList[j] == 0):
            break
        if j==len(pList)-1:
            pList.append(i)
print(sum(pList))
#this program just took way too long to compile so I stopped it.
#apparently there is a premade list of primes in the Python library
#but I did not want to use that.
