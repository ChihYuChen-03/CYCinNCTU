'''
Desc
輸入數個成績，如果 60（含）以上，則輸出 Pass，不到 60 ，則輸出 Fail，若小於 0 或大於 100，則輸出 Error。

Hint
1. split input as scores
2. use loop to go through all score in scores
3. use if-elif-else to determine Pass / Fail / Error
'''
'''
input: 78 50 101 -10 
--> 
output: 
Pass
Fail
Error
Error
'''
ls = list(map(int, input().split()))
for i in ls:
    if i > 100 or i < 0: 
        print('Error')
    elif i < 60: 
        print('Fail')
    else:
        print('Pass')