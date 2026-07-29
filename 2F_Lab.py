emails = 'cat@yahoo.com.tw, dog@google.com, tiger@icloud.com'
temp = emails.split(',')
print(temp[1])
# =============================Stack practice===========================
import random
ls = []
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)
# push
ls.append(num1)
ls.append(num2)
ls.append(num3)
# print(ls)

# pop
ls.pop()
print(ls)
# ========================================================
import random

def push_random(stack, n):
    for _ in range(n): # Python 開發者習慣用_ 當作變數名稱，代表「這個變數我不會用到，只是佔位符（placeholder）」，是一種常見的慣例（convention），讓程式碼更清楚地表達「這個值故意被忽略」。
        stack.append(random.randint(1, 10))

my_stack = []
push_random(my_stack, 3)
my_stack.pop()
push_random(my_stack, 2)
print(my_stack)

# ========================================================
import random

my_stack = []

for i in range(3):
    my_stack.append(random.randint(1, 10))
print("放入三個後：", my_stack)

pop_num = my_stack.pop()
print("拿出的整數：", pop_num)
print("目前 Stack：", my_stack)

for i in range(2):
    my_stack.append(random.randint(1, 10))

print("最後 Stack：", my_stack)
# ========================================================
import random

my_stack =[]

num1 = random.randint(1,10)
my_stack.append(num1)
num2 = random.randint(1,10)
my_stack.append(num2)
num3 = random.randint(1,10)
my_stack.append(num3)

poped_1 = my_stack.pop()

num4 = random.randint(1,10)
my_stack.append(num4)
num5 = random.randint(1,10)
my_stack.append(num5)

print(my_stack)