'''
Desc
請將輸入的數字中重複的元素移除，並且將數字由小到大排列

Hint
set() to remove duplicated elements
list.sort() to sort elements
str.join() to generate out string
'''
# input: 4, 9, 2, 4, 3, 7, 2 --> output: 2, 3, 4, 7, 9
nums = set(input().split(', '))
# print(nums)

result = list(nums)
result.sort()

# print(', '.join(result))
print(*result, sep = ", ") # ＊是解包
