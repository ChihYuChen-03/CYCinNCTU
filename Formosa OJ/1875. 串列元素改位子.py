'''
Desc
將List中最右邊的元素移動到最左邊
'''
# input: 1 2 3 4 5 --> output: [5, 1, 2, 3, 4]
nums = list(map(int, input().split()))
result = nums[-1:] + nums[:-1]
print(result)