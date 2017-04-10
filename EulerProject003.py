i=2
num = 600851475143 
while (num != i):
    if num%i == 0:
        num = num//i
    i+=1

print(num)
