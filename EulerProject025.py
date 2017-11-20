F1 = 1
F2 = 1
count = 1

while True:
    F3 = F1 + F2
    F1 = F2
    F2 = F3
    
    count += 1
    
    if len(str(F1)) == 1000:
        break

print(count)
