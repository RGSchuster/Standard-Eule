powers = {x:x**5 for x in range(10)}
passed = []

for i in range(2,500000):
    tempNum = str(i)
    count = 0
    for j in range(len(tempNum)):
        count += powers[int(tempNum[j])]
    if count==i:
        passed.append(i)

print(sum(passed))
