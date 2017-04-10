nums = [1,2]
evenSum = []
i=1
j=1
while (max(nums) < 4000000):
    a=nums[i-1]
    b=nums[i]
    c=a+b
    nums.append(c)
    i+=1
nums = nums[0:i]
while (j<len(nums)):
    if nums[j]%2==0:
        evenSum.append(nums[j])
    j+=1

print(sum(evenSum))
