#Make a prime list until my list is of length 10000
pList = [2]
for i in range(3,10000000):
    for j in range(0,len(pList)):
        if (i%pList[j] == 0):
            break
        if j==len(pList)-1:
            pList.append(i)
    if (len(pList)==10000):
        break
print(max(pList))
