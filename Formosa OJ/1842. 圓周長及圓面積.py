'''
Desc
給定一個圓的半徑 r, 印出該圓的圓周長和圓面積

Hint
圓周長 = 2 * 3.14 * 半徑
圓面積 = 3.14 * 半徑 * 半徑
round() 到小數第二位
'''
'''
input: 1.2
-->
output:
圓面積: 4.52
圓周長: 7.54
'''
r = float(input())
print(f'圓面積: {round(3.14*r*r, 2)}')
print(f'圓周長: {round(2*3.14*r, 2)}')