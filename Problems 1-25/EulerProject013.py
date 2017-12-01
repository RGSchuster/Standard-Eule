#I have the numbers saved in a .txt file.
#I will read them in as strings, take the first 13 digits,
#turn those into ints, and sum them.
#Finally, I will read the first 10 digits of the result
#by turning to a string to shorten

nums = []
with open('p013_numbers.txt') as f:
    for line in f:
        nums.append([v for v in line.split()])

for i in range(len(nums)):
    nums[i] = int(nums[i][0][:13])

print(int(str(sum(nums))[:10]))
