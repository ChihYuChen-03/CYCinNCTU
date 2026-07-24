'''
Desc
一年忠班的學藝股長選舉的投票投票結果如下: ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john", "john", "jamie"], 也就是 john 一票, johnny一票, jackie 一票, johnny 一票, john 一票,….., 請寫程式統計計票結果,
'''
'''
input: john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john john jamie 
--> 
output: 
john 5
johnny 4
jackie 2
jamie 4 
'''

names = list(input().split())
