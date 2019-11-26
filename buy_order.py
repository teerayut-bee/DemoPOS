def Buy_main():
    global buy_main
    file = open("buy_main.txt", "r", encoding="utf-8")
    buy_main = file.read().splitlines()
    file.close()

def Buy_detail():
    global buy_detail
    file = open("buy_detail.txt", "r", encoding="utf-8")
    buy_detail = file.read().splitlines()
    file.close()

def Order_Menu():
    global order_menu
    order_menu = ""
    order_menu = input("S = Show_Detail, D = Delete, C = Clear, B = Back : ").upper()

def Show_MainOrder():
    Buy_main()
    def Order_main():
        Buy_main()
        print("|", "-" * 97, "|")
        print("|", "Main Order".center(97), "|")
        print("|", "-" * 97, "|")
        print("|", "NO".center(5), "|", "OrderID".center(10), "|", "Date".center(20), "|", "Time".center(10), "|",
              "Seller".center(10), "|", "Item Total".center(12), "|","Price Total".center(12), "|")
        print("|", "-" * 97, "|")

        if len(buy_main) == 0:
            print("|", "No Item".center(100), "|")
        count = 0
        item_total=0
        price_total=0
        for x in buy_main:
            new_BuyMain = x.split()
            count = count + 1
            print("|", str(count).center(5), "|", new_BuyMain[0].ljust(12), new_BuyMain[1].ljust(22), new_BuyMain[2].center(10),
                  new_BuyMain[3].center(12), new_BuyMain[4].rjust(14), new_BuyMain[5].rjust(14),"|")
            item_total = item_total + int(new_BuyMain[4])
            price_total = price_total + int(new_BuyMain[5])

        print("|", "-" * 97, "|")
        print("|", "Total : ".rjust(43) + str(item_total).rjust(5), "Item  ", "total :".rjust(26),
              str(price_total).rjust(14), "|")
        print("|", "-" * 97, "|")


    def Order_detail():
        order_menu = ""
        order_menu = input("กรุณากรอก OrderID ที่ต้องการแสดง : ").upper()

        list_orderID,list_orderDate,list_orderTime,list_orderSeller=[],[],[],[]
        Buy_main()
        for x in buy_main:
            new_MainOrder = x.split()
            list_orderID.append(new_MainOrder[0])
            list_orderDate.append(new_MainOrder[1])
            list_orderTime.append(new_MainOrder[2])
            list_orderSeller.append(new_MainOrder[3])
        if order_menu in list_orderID:
            pos = list_orderID.index(order_menu)
            Buy_detail()
            new_orderID = []
            data = []
            for x in buy_detail:
                new_OrderDetail = x.split()
                new_orderID = new_OrderDetail[0]
                if order_menu == new_orderID:
                    data.append(x)

            print(" ", "-" * 83)
            print("|", "DemoPOS".center(82), "|")
            print("|", "  Sales number : ".rjust(17) + str(list_orderID[pos]), "Date : ".rjust(48) + str(list_orderDate[pos]), "|")
            print("|", "  seller : ".rjust(17) + str(list_orderSeller[pos]), "Time : ".rjust(49) + str(list_orderTime[pos]), "น.  ", "|")
            print("|", "-" * 82, "|")
            print("|", "NO".center(5), "|", "barcode".center(10), "|", "name".center(20), "|", "Price".center(10),
                    "|", "Unit".center(10), "|", "Total".center(12), "|")
            print("|", "-" * 82, "|")

            if len(data) == 0:
                print("|", "No Item".center(82), "|")
            count = 0
            global item_total
            item_total = 0
            global price_total
            price_total = 0
            for x in data:
                show = x.split()
                count = count + 1
                print("|", str(count).center(5), "|", show[1].ljust(12), show[2].ljust(22), show[3].center(10),
                        show[4].center(12), show[5].rjust(14), "|")
                item_total = item_total + int(show[4])
                price_total = price_total + int(show[5])

            print(" ", "-" * 83)
            print("|", "Total : ".rjust(33) + str(item_total).rjust(5), "Item  ", "total :".rjust(23),
                    str(price_total).rjust(12), "|")
            print(" ", "-" * 83)
            order_menu = ""
            while order_menu != "D" and order_menu != "B":
                order_menu = input("D = Delete, B = Back : ").upper()
                if order_menu == "D":
                    confirm = ""
                    while confirm != "Y" and confirm != "N":
                        confirm = input("คุณต้องการลบ Order : %s ใช่หรือไม่ (Y/N) : "%str(list_orderID[pos])).upper()
                        if confirm == "Y":
                            Delete_order(pos)
                        elif confirm == "N":
                            print("ยกเลิกการลบข้อมูล")
                        else:
                            print("กรุณากด Y หรือ N เท่านั้น!!!")
                elif order_menu == "B":
                    break
                else:
                    print("กรุณาเลือกเมนู D หรือ B เท่านั้น!!!")

        else :
            print("ไม่มี OrderID นี้อยู่ในระบบ!!!")

    def Delete_order(position_Order):
        Buy_main()
        Buy_detail()
        buy_main.pop(position_Order)
        pop_count = 0
        for x in buy_detail:
            delete_detail = x.split()
            if position_Order == delete_detail[0]:
                buy_detail.pop(pop_count)
            pop_count = pop_count + 1

        f_buy_main = open("buy_main.txt", "w", encoding="utf-8")
        f_buy_detail = open("buy_detail.txt", "w", encoding="utf-8")
        for x in buy_detail:
            ex = x.split()
            f_buy_detail.write("%s %s %s %s %s %s\n" % (ex[0], ex[1], ex[2], ex[3], ex[4], ex[5]))
        for x in buy_main:
            ex = x.split()
            f_buy_main.write("%s %s %s %s %s %s\n" % (ex[0], ex[1], ex[2], ex[3], ex[4], ex[5]))

        print("> ลบรายการเรียบร้อย <")
        f_buy_detail.close()
        f_buy_main.close()



    order_menu = ""
    while order_menu != "B":
        Order_main()
        order_menu = ""
        order_menu = input("S = Show_Detail, D = Delete, C = Clear, B = Back : ").upper()

        if order_menu == "S":
            Order_detail()
        elif order_menu == "D":
            Buy_main()
            search_id=[]
            for x in buy_main:
                search = x.split()
                search_id.append(search[0])
            order_menu = input("กรุณากรอก OrderID ที่คุณต้องการลบ : ").upper()
            if order_menu in search_id:
                position_delete = search_id.index(order_menu)
                confirm = ""
                while confirm != "Y" and confirm != "N":
                    confirm = input("คุณต้องการลบ Order : %s ใช่หรือไม่ (Y/N) : " % str(order_menu)).upper()
                    if confirm == "Y":
                        Delete_order(position_delete)
                    elif confirm == "N":
                        print("ยกเลิกการลบข้อมูล")
                    else:
                        print("กรุณากด Y หรือ N เท่านั้น!!!")
            else :
                print("ไม่มี OrderID นี้อยู่ในระบบ!!!")
        elif order_menu == "C":
            confirm = ""
            while confirm != "Y" and confirm != "N":
                confirm = input("คุณต้องการลบ Order : %s ใช่หรือไม่ (Y/N) : " % str(order_menu)).upper()
                if confirm == "Y":
                    f_buy_main = open("buy_main.txt", "w", encoding="utf-8")
                    f_buy_detail = open("buy_detail.txt", "w", encoding="utf-8")
                    f_buy_detail.write("")
                    f_buy_main.write("")
                    print("> ล้างรายการเรียบร้อย <")
                    f_buy_detail.close()
                    f_buy_main.close()
                elif confirm == "N":
                    print("ยกเลิกการลบข้อมูล")
                else:
                    print("กรุณากด Y หรือ N เท่านั้น!!!")

        elif order_menu == "B":
            break
        else:
            print("กรุณาเลือกเมนูใหม่อีกครั้ง!!!")

Show_MainOrder()








