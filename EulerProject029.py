terms = []

#This brute forces all powers
#Ranges are from 2 to 101 because we need to include 100
for a in range(2,101):
    temp = [a**2]
    for b in range(3,101):
        temp.append(temp[-1]*a)
    terms = list(set(terms+temp))

print(len(terms))
