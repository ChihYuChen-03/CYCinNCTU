'''
Desc
寫一段程式將Input中的字串輸出成Output中的字串
'''
# input: learning python --> output: Learning_Python
tmp = input().split()
tmp[0] = tmp[0].capitalize()
tmp[1] = tmp[1].capitalize()
print(tmp[0] + '_' + tmp[1])