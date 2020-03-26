"""
x = 3;
y = float(x);
print(y);
"""
'''
mathScore = [60,70,10,20,81,63] #index分別為0,1,2,3,4,5
print(mathScore[2]) #會出現10
print(mathScore[1:6]) #會出現第1到第5的數字  6(右邊數字)不包含
print(mathScore[-1]) #會出現倒數第一個數字
print(mathScore[:5]) #數字沒打代表0
print(mathScore[5:]) #5到最後
print(len(mathScore)) #個數
print(sum(mathScore))
print(max(mathScore))
print(min(mathScore))
print(sum(mathScore)/len(mathScore))

mathScores2 = []
print(mathScores2)
mathScores2.append(60)
print(mathScores2)
mathScores2.append(70)#append:對於list 往最右邊一直加數字上去
mathScores2.append(50)
mathScores2.append(40)
mathScores2.insert(2,30) #在第2的地方插入30 insert:在中間插入數字
print(mathScores2)
mathScores2.remove(70) #刪除70
print(mathScores2)
del mathScores2[2] #刪除index2的數字
del mathScores2[2:4] #刪除index2和3的數字
print(mathScores2)

mathScores2[1]=55 #把index1的值修改為50
print(mathScores2)
mathScores2.append(70)
mathScores2.append(40)
print(mathScores2)
print(mathScores2.count(40)) #查詢40這個數字在list裡面總共有幾個
print(mathScores2.index(40)) #第一個遇到的40index為多少
print(mathScore)
print(mathScores2)
print(mathScore+mathScores2) #兩個list相加 後面的接在右邊
print(sorted(mathScores2)) #升冪
print(sorted(mathScores2,reverse=True)) #降冪

ls = [[1,2,3],[4,5,6]] #巢狀list
print(ls[0]) #顯示list中index為0的小list
print(ls[0][2]) #顯示index為0的list中index為2的值


"""
mathScores2.pop() #刪除最右邊的值 pop:刪除
print(mathScores2)
mathScores2.pop(1) #刪掉index1的值
print(mathScores2)
"""

print(33 in mathScores2) #查看33是否在裡面(true or false)
print(55 not in mathScores2)


#小練習
grades = [[5,14,7],[23,36,28],[88,80,92]]
print(grades[2])
print(sum(grades[0])/len(grades[0]))
print(sum(grades[1])/len(grades[1]))
print(sum(grades[2])/len(grades[2]))
grades.append([94,90,96])
print(grades)
grades[0][1]=20
print(grades)
'''

#-----tuple------
'''
tuple1 = (1,2,3,4,5) #tuple為()  list為[]
tuple2 = 1,2,3,4,5  #兩個一樣(可以括號也可以不括號)
print(tuple1)
print(tuple2)
print(tuple1[3]) #顯示tuple1中index為3的值
print(tuple1.index(4)) #數字4在tuple1的第一個undex為多少
print(tuple1.count(3)) #數字3有幾個
"""
tuple1[2] = 10 #會出現error  tuple不能像list一樣更改、新增(append)、刪除(remove)值
print(tuple1)
"""

tuple1 = (1,2,3,4,5)
tuple2 = (3,3,4,5,6)
print(tuple1+tuple2)
print(sorted(tuple1,reverse=True))
print(1 in tuple1) #1是否在tuple1裡

tuple3 = ()
print(tuple3)

tuple1=(88,12,20)
x,y,z = tuple1
print(x)
print(y)
print(z)


#小練習
gradesTuple = ((5,14,7),(23,36,28),(88,80,92))
print(gradesTuple[2])
print(sum(gradesTuple[0])/len(gradesTuple[0])) #index幾乎都是用中括號
print(sum(gradesTuple[1])/len(gradesTuple[1]))
print(sum(gradesTuple[2])/len(gradesTuple[2]))
'''


#----Dictionary-----
"""
family = {
    'dad': 'Homer',
    "mom": "Marge",  #單引或雙引號都可以
    'son': 'Bart',
    'daughter': 'Lisa'
}
print(family["dad"])
print(family.get("dad"))
"""
#print(family["dog"])
#print(family.get("dog")) #通常使用這個比較好找錯誤
"""
print('dad' in family)
print(family.keys()) #顯示所有的Key
print(family.values()) #顯示所有的value
print(family.items()) #顯示所有配對的key-value

family = {}
print(family)
family["cousin"] = "Max"  #新增一個
print(family)
family["cousin"] = "Eric" #key不能重複 所以Max會被改成Eric
print(family)
family.update({  #一次新增多個
    "uncle": "Martin",
    "aunt": "May"
})
print(family)

del family["uncle"] #刪除uncle
print(family)
family.pop("cousin") #刪除cousin
print(family)

#小練習
gradesDict = {
    'chinese': [5,14,7],  #不能打為'chinese': '[5,14,7]'  因為' '代表字串，這樣list會變成字串
    'english': [23,36,28],
    'math':[88,80,92]
}
print(gradesDict["math"])
print(sum(gradesDict['chinese'])/len(gradesDict['chinese']))
print(sum(gradesDict["english"])/len(gradesDict["english"]))
print(sum(gradesDict["math"])/len(gradesDict["math"]))
gradesDict["science"] = [94,90,96]
print(gradesDict)
"""


#---set-------
"""
fruits = {
    'apple',
    'banana',
    'guava'
    'guava'
}
fruits1 = {
    "strawberry",
    "papaya",
    "banana"
}
print(fruits|fruits1)
fruits.add("watermelon")
print(fruits)
fruits.remove("watermelon")
#fruits.discard("watermelon") #discard=remove
print(fruits)
print(sorted(fruits)) #排序(回傳list)
fruits.clear() #清除全部(變空集合)
print(fruits)

#小練習
allStudents = {
    'John','Eva','Jill','Eric','Andy','Albert','Polina','Kristin','Angela'
}
guitarClub = {'John','Eva','Jill','Eric','Andy'}
danceClub = {'Albert','Polina','Eric','Andy','Kristin'}
print(danceClub&guitarClub)
print(guitarClub-danceClub)
both = guitarClub|danceClub
print(allStudents-both)
"""
print("hello hello")
print("hello hello")
print("hello hello")


