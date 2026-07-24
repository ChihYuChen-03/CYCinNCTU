'''
Desc
請寫一個美元兌換台幣的程式，將一個list內的各個美元計價的商品，計算出台幣計價的價格
'''
''' 
input:
31.32
1 10 100
--> 
output: 
31
313
3132
'''
exchange = float(input())
us_price = list(map(int, input().split()))

ls = []
for i in us_price:
    final_price = int(exchange * i)
    print(final_price)