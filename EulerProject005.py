i = 18
count,interval = 19*20,19*20
while i>3:
    
    if count%i == 0:
        i-=1
        interval = count
    else:
        count+=interval
print(count)
