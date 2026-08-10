'''
Desc
統計生日快樂歌詞內各個字出現的次數
'''
'''
input: Happy birthday to you Happy birthday to you Happy birthday, happy birthday Happy birthday to you 
--> output: 
happy 5
birthday 5
to 3
you 3
'''
words = input().lower().replace(',', '').split()
# print(words)
dt = {}
for word in words:
    if word in dt.keys():
        dt[word] += 1 # 對已存在的 key，更新它的 value
    else:
        dt[word] = 1 # 新增一個全新的 key-value 配對
for i, obj in dt.items():
    print(i , obj)
