'''
Desc
輸入一個整數, 輸出月份名稱

Hint
use list or dict instead of if condition
'''
# input: 2 --> output: Feb
months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
usr_input = int(input())
while usr_input < 1 or usr_input > 12: # n, an integer, 1 <= n <= 12
    usr_input = int(input())
print(months.get(usr_input))