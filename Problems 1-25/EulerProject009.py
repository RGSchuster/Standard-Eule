import math
max = 0
for a in range(3,300): #runs through all a and b values that would work for a+b+c=1000
    for b in range(4,400):
        c = math.sqrt(a**2 + b**2)
        if (c/1)==c:#checks if c is an integer
            if (a+b+(c/1))==1000:
                print(a*b*(c/1))
