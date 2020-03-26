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

while flag:  #當true的時候會執行以下程式
    print("\n==========================")
    select = eval(input("1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:"))

    if select == 1:  #儲值
        value = eval(input("儲值金額:"))
        while value < 1:
            #若使用者輸入數字小於零，需要重新輸入
            print("====儲值金額需大於零====")
            value = eval(input("儲值金額:"))
        balance += value
        print(f"儲值後餘額為{balance}元") #'pass'的功能為代替像java的大括號({}) 用於將程式區分開

    elif select == 2:  #購買
        #印出品項
        print("\n請選擇商品")
        for i in range(0, len(drinks)):
            print(f'({i + 1})\t{drinks[i]["name"]} \t {drinks[i]["price"]}元')
        choose = eval(input("請選擇編號:"))

        while choose < 1 or choose > 6:
            print("====清輸入1-6之間====")
            choose = eval(input("請選擇:"))

        buy_drink = drinks[choose-1]
        if balance < buy_drink["price"]:
            print("====餘額不足====")
        else:
            print(f'已購買{buy_drink["name"]}  {buy_drink["price"]}元')
            balance -= buy_drink["price"]
            print(f'購買後餘額為{balance}元')

    elif select == 3:  #查詢餘額
        print(f"目前餘額為{balance}元")

    elif select == 4:  #離開
        print("bye")
        flag = 0
        break

    else:  #重新輸入
        print("====請輸入1~4之間====")
        continue

#函式 : 將一段程式群組起來，以後需要用到那一段程式的功能時，打出他的函示就好，
#比較快速，要修改程式時也比較快速不用一個一個改