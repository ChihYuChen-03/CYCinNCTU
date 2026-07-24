'''
Desc
輸入一連串的工作年資，找出最資淺的年資是多少

Hint
使用List來放年資列表: x = list(map(int, input().split(',')))
使用f-string來格式化輸出
'''
# input: 8, 1, 2, 5, 3, 6, 9, 3 --> output: 最菜鳥的工作年資是1年
ls = list(map(int, input().split(',')))
# print(ls)
year = min(ls)
print(f'最菜鳥的工作年資是{year}年')