'''
Desc
請寫一個美元兌換台幣的函式，並使用此函式將一個list內的各個美元計價的商品，計算出台幣計價的價格
'''
'''
input:
31.32
1 10 100
-->
output:
us_price:1, tw_price:31
us_price:10, tw_price:313
us_price:100, tw_price:3132
'''
exchange = float(input())
us_price = list(map(int, input().split()))

ls = []
for i in us_price:
    final_price = int(exchange * i)
    # ls.append(final_price)
    print(f'us_price:{i}, tw_price:{final_price}')