'''
Desc
[維基百科，自由的百科全書]
迴文，亦稱回文、回環，是正讀反讀都能讀通的句子，亦有將文字排列成圓圈者，是修辭方式和文字遊戲。運用得當可以表現兩種事物或現象相互依靠或排斥的關係。
以下是迴文的例子
. 上水居民居水上
. 花蓮噴水池水噴蓮花
. 上海自來水來自海上
判斷輸入的句子是否為迴文

Hint
全改成小寫並去掉空白
使用 string indexing [::-1]
'''
# input: 情人 --> output: False
# input: 山東落花生花落東山 --> output: True
# input: Was it a car or a cat I saw --> output: True
words = input().lower().replace(' ', '')
# print(words)
if words == words[::-1]:
    print('True')
else:
    print('False')