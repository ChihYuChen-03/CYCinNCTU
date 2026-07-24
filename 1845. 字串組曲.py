'''
Desc
使用字串函式，將input的四個字串加在一起，請注意大小寫
'''
# input: nycu python class HA --> output: NYCU Python Class haha
# nycu python class HA
n1, n2, n3, n4 = input().split()
n1 = n1.upper()
n2 = n2.capitalize()
n3 = n3.capitalize()
n4 = n4.lower() *2
print(n1, n2, n3, n4)