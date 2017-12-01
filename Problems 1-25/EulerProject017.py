#I want to use memoization to store a list of all the numbers
#and how many letters their sum is. This way I can test any value (up to 1000).
#For this problem, I shall count up to 1000 and then just print the last value of my list

ValueToSum=1000
tracker = [0]

def singles(curVal):
    #checks the values 0-9 then outputs count for letters
    if (curVal==1) | (curVal==2) | (curVal==6):
        return 3 #one, two, six
    elif (curVal==4) | (curVal==5) | (curVal==9):
        return 4 #four, five, nine
    elif (curVal==3) | (curVal==7) | (curVal==8):
        return 5 #three, seven, eight
    else:
        return 0 #numbers divisible by 10 have no extra wording on them

def doubles(curVal):
    #sends all single digit numbers to the 'singles' function
    #then checks the values 10-99 then outputs count for letters
    #first part is for 11-19 because of weird English language rules
    #second part is for 20-99
    if (curVal<10) & (curVal>0):
        return singles(curVal)
    elif (curVal==10):
        return 3 #ten
    elif (curVal==11) | (curVal==12):
        return 6 #eleven, twelve
    elif (curVal==15) | (curVal==16):
        return 7 #fifteen, sixteen
    elif (curVal==13) | (curVal==14) | (curVal==18) | (curVal==19):
        return 8 #thirteen, fourteen, eighteen, nineteen
    elif (curVal==17):
        return 9 #seventeen
    elif ((curVal//10)==7):
        return (7 + singles(curVal%10)) #seventy
    elif ((curVal//10)==4) | ((curVal//10)==5) | ((curVal//10)==6):
        return (5 + singles(curVal%10)) # forty, fifty, sixty
    elif ((curVal//10)==2) | ((curVal//10)==3) | ((curVal//10)==8) | ((curVal//10)==9):
        return (6 + singles(curVal%10)) #twenty, eighty, ninety
    else:
        return -3 #numbers divisible by 100 need to lose 3 because they don't have the word "and"

for i in range(1, ValueToSum+1):
    if i<10:
        tracker.append(tracker[i-1] + singles(i))
    elif i<100:
        tracker.append(tracker[i-1] + doubles(i))
    elif i<1000:
        tracker.append(tracker[i-1] + singles(i//100) + 10 + doubles(i%100)) #"hundred and" has 10 letters
    elif i==1000:
        tracker.append(tracker[i-1] + 11) #"one thousand" has 11 letters
        
print(tracker[ValueToSum])
