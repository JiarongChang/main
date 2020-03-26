#建立函式(function)改寫
flag = True
balance = 0
drinks = [
        {"name":"可樂","price":20},
        {"name":"雪碧","price":20},
        {"name":"茶裏王","price":25},
        {"name":"原萃","price":25},
        {"name":"純粹喝","price":30},
        {"name":"水","price":20},
]
def deposit():
    global  balance #全域變數
    # global balance: 告訴這個函式的balance變數為函式外面的變數，
    # 否則balance會有紅線，因為函示是完全獨立的，函式裡的變數和函式外的變數是分開的
    value = eval(input("儲值金額:"))
    while value < 1:
        print("====儲值金額需大於零====")
        value = eval(input("儲值金額:"))
    balance += value
    print(f"儲值後餘額為{balance}元")

def buy():
    global balance,drinks #需要兩個全域變數
    print("\n請選擇商品")
    for i in range(0, len(drinks)):
        print(f'({i + 1})\t{drinks[i]["name"]} \t {drinks[i]["price"]}元')
    choose = eval(input("請選擇編號:"))

    while choose < 1 or choose > 6:
        print("====清輸入1-6之間====")
        choose = eval(input("請選擇:"))

    buy_drink = drinks[choose - 1]
    while balance < buy_drink["price"]:
        print("====餘額不足，需要儲值嗎====")
        want_deposit = input("y/n?")
        if want_deposit == "y":
            deposit()
        elif want_deposit == "n":
            break
        else:
            print("====請重新輸入====")

    if balance >= buy_drink["price"]:
        print(f'已購買{buy_drink["name"]}  {buy_drink["price"]}元')
        balance -= buy_drink["price"]
        print(f'購買後餘額為{balance}元')

while flag:  #當true的時候會執行以下程式
    print("\n==========================")
    select = eval(input("1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:"))

    if select == 1:  #儲值
        deposit()

    elif select == 2:  #購買
        buy()  #按著ctrl在對'buy'按左鍵可以看到buy()的函式

    elif select == 3:  #查詢餘額
        print(f"目前餘額為{balance}元")

    elif select == 4:  #離開
        print("bye")
        flag = 0
        break

    else:  #重新輸入
        print("====請輸入1~4之間====")
        continue
"""
#函式 : 將一段程式群組起來，以後需要用到那一段程式的功能時，打出他的函示就好，
#比較快速，要修改程式時也比較快速不用一個一個改


weight1 = 100
weight2 = 80
def add_weight(w1,w2):
    result = w1+w2
    return result
x = add_weight(weight1,weight2)  # w1=weight1  w2=weight2 (參數位置對應)
print(x)


weight1 = 100
weight2 = 80
def add_weight(w1,w2=1):  #當w2已經預設等於1時，下面呼叫函式時括號裡的參數可以只打一個(weigh1)，而weight2=1
    result = w1+w2
    return result
x = add_weight(weight1)
print(x)


weight1 = 100
weight2 = 80
def add_weight(w1,w2):
    result = w1+w2
    result1 = w1 / w2
    return result,result1
x = add_weight(weight1,weight2)
r1,r2 = add_weight(weight1,weight2)  # w1=weight1,w2=weight2
y1,y2 = add_weight(w2=weight1,w1=weight2) #將順序調換
print(x)  #print出來會是tumple的形式=>(180,8000)
print(r1,r2)  #print出來會是數字的形式=>180,8000
print(y1,y2)
"""