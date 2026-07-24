'''
Desc
有三個點, 座標分別為(1, 1), (3, 4), (5, 3), 請計算出哪一個點跟座標為 (2.5, 2.5)的點的距離最遠？
'''
# input: none --> output: (5, 3) 距離為2.55
#print((2.5**2+0.5**2)**0.5)
def point_cal(x, y):
    Distance = ((2.5-x)**2 + (2.5-y)**2)**0.5
    return Distance

ls = [(1, 1), (3, 4), (5, 3), (1,2)]
result = []
for i in range(len(ls)):
    # print(ls[1][0], ls[1][1])
    result.append(point_cal(ls[i][0], ls[i][1]))
    z = (ls[i], result[i])
    # print(z)
    
max_distance = max(result)
max_index = result.index(max_distance)
max_point = ls[max_index]
# print(max_index, max_point)
print(f'{max_point} 距離為{max_distance :.2f}')