powerStr = str(2**1000) #builds a string of the number 2^1000
digitSum = 0
for i in range(len(powerStr)):
    digitSum += int(float(powerStr[i]))
print(digitSum)
