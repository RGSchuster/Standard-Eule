#For any nxm grid
import math
n,m = 20,20
a = math.factorial(n+m)
b = math.factorial(n)
c = math.factorial(m)
num = a/(b*c)
print(num)
