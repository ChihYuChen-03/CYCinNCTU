'''
Desc
最小公倍數(least common multiple，lcm) 是數論中的一個概念。若有一個數 X ，可以被另外兩個數 A、B 整除，且 X 同時大於或等於 A 和 B，則 X 為 A 和 B 的公倍數。 A 和 B 的公倍數有無限個，而所有正的公倍數中，最小的公倍數就叫做最小公倍數
'''
# inout: 8 10 --> output: LCM: 40
# LCM n1, n2 

a, b = map(int, input().split())
x = max(a, b)

while True:
    if x%a == 0 and x%b == 0: 
        print(f'LCM: {x}')
        break
    x += 1