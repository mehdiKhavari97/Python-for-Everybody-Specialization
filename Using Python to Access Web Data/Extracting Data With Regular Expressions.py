import re

fhand = open('regex_sum_1255208.txt') #replace it with your file location
sum = 0
for line in fhand:
    nums = re.findall('[0-9]+', line)
    if len(nums)>0:
        for num in nums:
            sum += int(num)
print(sum)
