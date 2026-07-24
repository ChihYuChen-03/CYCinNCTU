'''
Desc
輸入一個數字 n, 計算 n!
'''
# input: 4 --> output: 24
tmp = int(input())
final = tmp
while tmp > 1:
    i = tmp - 1
    final *= i
    tmp -= 1
print(final)