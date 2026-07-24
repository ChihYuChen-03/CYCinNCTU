'''
Desc
輸入一個整數，將這個整數每個位數相加
123 -> 1+2+3 -> 6
2345 -> 2+3+4+5 -> 14
'''
# input: 123 --> output: 6
# input: 4167 --> output: 18
nums = list(map(int, input().strip()))
i = 0
for num in range(len(nums)):
    i += nums[num]
print(i)