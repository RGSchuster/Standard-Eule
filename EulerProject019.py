##dic = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
##cal = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
##
##day = 1
##year = 1900
##strtYear = 1901
##stopYear = 2000
##
##print(dic['Jan'])
##print(cal)

# Instead of caring about how many days are in a month,
# I just care about the remainder when the days are divided by 7.
# That way I can keep track of my month start day as I move through the year.
# I use nested loops to cycle through the years
months = [3,0,3,2,3,2,3,3,2,3,2,3]
day = 2
Oyear = 1900
startYear = 1901
stopYear = 2000
counter = 0

for i in range(Oyear,startYear):
    for j in range(len(months)):
        day += months[j]
        if (j==1) & ((i%4)==0) & ((i%100)!=0):
            day += 1
        if day>7:
            day -= 7

for year in range(startYear,stopYear+1):
    for x in range(len(months)):
        if day == 1:
            counter += 1
        day += months[x]
        if (x==1) & ((year%4)==0) & ((year%100)!=0):
            day += 1
        if (x==1) & ((year%400)==0):
            day += 1
        if day>7:
            day -= 7
print(counter)
