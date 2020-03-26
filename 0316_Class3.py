"""
x = 4**0.5
print(x)

import math
print(math.sqrt(5.8))

#小練習
r = 3
circlearea = r**2*3.14
print(circlearea)
scores = [10,30,40,90,100,60]
avg = sum(scores)/len(scores)
print(avg)


score = 60
if score >= 60: #python用冒號(:)來代表執行以下程式 下面的程式前面需要空格
    print("及格")
else:
    print("不及格")

score = 98
if score >= 60:
    print("及格")
    if score >= 90:  #巢狀條件
        print("你最棒了")
    else:
        print("還好還好")
elif 55 <= score < 60: #也可寫成elif 55 <= score and score < 60:
    print("拜託")
elif 50 <= score < 55:
    print("差一點")
else:
    print("不及格")


print("hello","world","!") #分開打會在每個字中自動加空格
print("hello\nworld\n!") #\n為換行
print("123",end="") #加上 end="" 會讓下一行的print直接接在後面 在""裡
print("456")  #顯示為123456
print("123",end="aaa") #在""裡加東西會讓它出現在此行及下行的print中間
print("456")  #顯示為123aaa456

x = 42
value = f"Value of x is {x}"
print(value)

mathScores = [60,70,10,20,81,63,4]
firstItem = f"first item in mathScores is {mathScores[0]}" #{}在可以打你想要顯示的東西
print(firstItem)
print(f"the mathScores has {len(mathScores)} items")

#迴圈
for i in range(0,10): #i會從0跑到9(因為最右邊的數字(10)不算 (變數 i 不須另外宣告!!
    print(i)
for i in range(10): #可省略 0
    print(i)
for i in range(0,10,3): #最後的數字代表間隔(會顯示0 3 6 9)
    print(i)
for i in range(len(mathScores)): #len(mathScores)為7 所以print出來的會是0到6
    print(i,mathScores[i]) #顯示i及對應的值
for i in mathScores: #較方便的寫法 直接把list的值print出來
    print(i)

family = {
    'dad': 'Homer',
    "mom": "Marge",
    'son': 'Bart',
    'daughter': 'Lisa'
}
for member in family.items():
    print(member)
for key,value in family.items():
        print(f"my{key} is {value}")

#小練習
mathScores = [60,70,10,20,81,63,4]
for score in mathScores:
    print(score**0.5*10)

import math
[print(math.sqrt(value)*10) for value in mathScores]

[print(k) for k in range(10)] #print出0到9 較快速的寫法


count = 0
while count < 10:
    print(count)
    count+=1

mathScores = [60,70,10,20,81,63,4]
for score in mathScores:
    if score > 80:
        break #整個迴圈跳掉 (所以81之後的分數不會再跑迴圈
    print(score)

mathScores = [60,70,10,20,81,63,4]
for score in mathScores:
    if score > 80:
        continue #只跳出一次for迴圈 (所以81之後的分數仍會繼續跑回圈
    print(score)

import random
i = random.randint(1,50)
print(i)
x = eval(input("How many rows:")) #輸入語法(eval為讓輸入的字串變成數字
print(type(x)) #type我不知道是什麼
"""
#小練習
"""
for m in range(1,10):
    print()
    for n in range(1,10):
        print(m,"*",n,"=",m*n,end="  ")

count=1
while count<=50:
    print("你好")
    count+=1
else:
    print("我說完了啦")

num = eval(input("Enter a number:"))
for i in range(1,num+1):
    if i % 2 != 0:
        print(i)

import random
ls=[]
row = eval(input("Enter row:"))
column = eval(input("Enter column:"))
for r in range(row):
    ls.append([])  # i=1 -> [[]] ; i= -> [[] []]
    for c in range(column):
        num = random.randint(1,100)
        ls[r].append(num)  #[[1 2 3] [4 5 6] [7 8 9]]
for x in range(row):
    for y in range(column):
        print(f"{ls[x][y]}",end=" ")
    print()

total = 0  #所有元素加總
for x in range(row):
    total=total+sum(ls[x])
print("total is:",total)

rowsum = 0  #每一列的總和
rowlist=[]
for x in range(row):
    rowsum = 0
    for y in range(column):
        rowsum = rowsum + ls[x][y]
    rowlist.append(rowsum)
print("row的總和:",rowlist)

colusum = 0  #每一行的總和
colulist = []
for y in range(column):
    colusum = 0
    for x in range(row):
        colusum = colusum + ls[x][y]
    colulist.append(colusum)
print("column的總和:",colulist)
"""
ls1 = [[1,2,3],
       [3,4,5],
       [5,6,7]]
ls2 = [[2,3,4],
       [4,5,6],
       [6,7,8]]
ls3=[]
for x in range(len(ls1)):
    ls3.append([])
    for y in range(len(ls1)):
        ls3[x].append(ls1[x][y] + ls2[x][y])
        print(f"{ls3[x][y]}",end=" ")
    print()