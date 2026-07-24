'''
Desc
根據勾股定理，直角三角形的兩個直角邊的平方和等於斜邊的平方
'''
# input: 5 3 4 --> output: Y
# input: 3 3 3 --> output: N
usr_input = list(map(int, input().split()))
temp = sorted(usr_input)

def pathagorean(a, b, c):
    if a**2 + b**2 == c**2:
        return 'Y'
    return 'N'

print(pathagorean(temp[0], temp[1], temp[2]))