# Instead of caring about how many days are in a month,
# I just care about the remainder when the number of days are divided by 7.
# That way I can keep track of my month start day as I move through the year.
# I use nested loops to cycle through the years
months = [3,0,3,2,3,2,3,3,2,3,2,3]
day = 2 #1=Sunday, 2=Monday, 3=Tuesday, etc
Oyear = 1900
startYear = 1901
stopYear = 2000
counter = 0
#This first loop starts at 1900 and counts up to my start year
for i in range(Oyear,startYear):
    for j in range(len(months)):
        day += months[j]
        if (j==1) & ((i%4)==0) & ((i%100)!=0):
            #this checks if the month is February and the year is divisible by 4 and NOT a century, then adds a day for leap
            day += 1
        if day>7:
            day -= 7
#The second loop goes in the requested time
for year in range(startYear,stopYear+1):
    for x in range(len(months)):
        if day == 1:
            counter += 1
        day += months[x]
        if (x==1) & ((year%4)==0) & ((year%100)!=0):
            day += 1
        if (x==1) & ((year%400)==0):
            #This checks if the month is February and the year is a century divisible by 400, then adds a day for leap
            day += 1
        if day>7:
            #resets day tracker to an actual day of the week
            day -= 7
print(counter)

#as with all programs, this can easily be modified to count the Sunday starts for any given year range
