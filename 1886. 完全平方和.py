'''
Desc
1、9、16、25、36、49，這些都是完全平方數, 請求出 1~30 裡面完全平方數的總和
'''
# input: None --> output: 55
total = 0
for i in range(1, 31):
    if i ** 0.5 %1 == 0 :
        total += i

print(total)