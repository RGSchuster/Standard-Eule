multiples = []
i = 2
while i<1000:
    if (i%3==0) | (i%5==0):
        multiples.append(i)
    i+=1
print(sum(multiples))
