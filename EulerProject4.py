def main():
    i,j,a,b = 999,999,0,0
    while a<200:
        while b<200:
            product = i*j
            if ((product%10 == product//100000) & ((product//100)%10 == (product//1000)%10) & ((product//10)%10 == (product//10000)%10)):
                print(product)
                return product
            i-=1
            b+=1
        i,b = 999,0
        j-=1
        a+=1

if __name__=='__main__':
    main()
