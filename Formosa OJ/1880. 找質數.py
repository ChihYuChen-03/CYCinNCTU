'''
Desc
找出20內的質數.(大於1的自然數中，除了1和該數自身外，無法被其他自然數整除的數)
'''
''' 
input: none 
--> 
output: 
2 is Prime
3 is Prime
5 is Prime
7 is Prime
11 is Prime
13 is Prime
17 is Prime
19 is Prime
'''
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

for num in range(1, 21):
    if is_prime(num) == True:
        print(f'{num} is Prime')