#I could not figure out how to split the text file at the commas,
#so I read it all in as one large item and split it later
file = open('p022_names.txt')
for f in file:
    names = f
file.close()
#Replace all quotation marks with nothing (essentially, delete them)
names = names.replace("\"","")

cleanNames = (names.split(","))
cleanNames.sort()

#I now have a sorted list of all names.
#Time to make a dictionary for each character and iterate through the list.
#I will build a new list of the numerical value for each name,
#then multiply by its index
#and finally sum the results

letters = dict(A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,J=10,K=11,L=12,M=13,N=14,O=15,P=16,Q=17,R=18,S=19,T=20,U=21,V=22,W=23,X=24,Y=25,Z=26)
count = 0

for i in range(len(cleanNames)):
    tempName = cleanNames[i]
    tempCount = 0
    for j in range(len(tempName)):
       tempCount += letters[tempName[j]]
    count += tempCount*(i+1) #adds sum of letters in name * number in list
print(count)
