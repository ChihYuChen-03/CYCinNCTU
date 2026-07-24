'''
Desc
給兩個數字以及一個運算符號（只會是加減乘除其中一個）求出計算結果
'''
# input: 6 * 2 --> output: 6 * 2 = 12
temp = input()
user_input = list(temp.split())

def operator(i, n , i1): 
    i = int(i)
    i1 = int(i1)
    if n == '+':
        return i + i1
    elif n == '-':
        return i - i1
    elif n == '*':
        return i * i1
    return i / i1

print(f'{temp} = {operator(user_input[0], user_input[1], user_input[2])}')