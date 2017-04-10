#I just made an infinite for loop. I can stop it manually if it runs too long
import math
def main():
    triNum = 1
    factors = 2
    i=2
    while True:
        triNum += i
        factors = 2
        sqroot = int(math.sqrt(triNum))
        if sqroot*sqroot == triNum:
            factors += 1
        for j in range(2,sqroot):
            if triNum%j==0:
                factors += 2
            if factors == 500:
                print (triNum)
                return triNum
        i+=1
if __name__=='__main__':
    main()
