#建立模組改寫
import vending_machine.vending_machine as machine  #有兩種匯入方式(詳見講義)

flag = True

while flag:  #當true的時候會執行以下程式
    print("\n==========================")
    select = eval(input("1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:"))

    if select == 1:  #儲值
        machine.deposit()

    elif select == 2:  #購買
        machine.buy()  #按著ctrl在對'buy'按左鍵可以看到buy()的函式

    elif select == 3:  #查詢餘額
        print(f"目前餘額為{machine.balance}元")

    elif select == 4:  #離開
        print("bye")
        flag = 0
        break

    else:  #重新輸入
        print("====請輸入1~4之間====")
        continue
