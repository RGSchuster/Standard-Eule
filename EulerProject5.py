i = 8
count = 9*10
interval = 90
while i>4:
    
    if count%i == 0:
        count = count*i
        i-=1
        interval = count
    else:
        count+=interval
print(count)
        
