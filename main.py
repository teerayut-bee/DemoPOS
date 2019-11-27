def Page_sell():
    def Buy_main():
        global buy_main
        file = open("buy_main.txt", "r", encoding="utf-8")
        buy_main = file.read().splitlines()
        file.close()

    def Product():
        global product
        file = open("product.txt","r", encoding="utf-8")
        product = file.read().splitlines()
        file.close()

    def Sell_menu():
        global sell_menu
        sell_menu=""
        sell_menu = input("V = แสดงข้อมูลการซื้อ, B = กลับสู่เมนูหลัก, S = แสดงสินค้าทั้งหมด, Enter = ทำรายการต่อ : ").upper()

    def View_Set():
        from datetime import datetime
        global dt_date, dt_time, new_order
        now = datetime.now()
        dt_date = now.strftime("%d/%m/%Y")
        dt_time = now.strftime("%H:%M")

        Buy_main()
        if len(buy_main) == 0:
            new_order = "N" + "1".rjust(5, "0")
        else:
            for x in buy_main:
                list_order = x.split()
                last_order = str(list_order[0])
            old_order = int(last_order[1:6])
            new_order = "N" + str(old_order + 1).rjust(5, "0")

    def View_Save():
        confirm = ""
        while confirm != "N" and confirm != "Y":
            confirm = input("คุณต้องการบันทึกข้อมูลใช่หรือไม่ (Y/N) : ").upper()
            if confirm == "Y":
                if len(buy_show) != 0:
                    f_buy_main = open("buy_main.txt", "a", encoding="utf-8")
                    f_buy_detail = open("buy_detail.txt", "a", encoding="utf-8")
                    for x in buy_show:
                        ex = x.split()
                        f_buy_detail.write("%s %s %s %s %s %s\n" % (new_order, ex[0], ex[1], ex[2], ex[3], ex[4]))
                    f_buy_main.write("%s %s %s %s %s %s\n" % (
                        new_order, str(dt_date), str(dt_time), str(show_username), str(item_total), str(price_total)))
                    print("> บันทึกสินค้าเรียบร้อย <")
                    f_buy_detail.close()
                    f_buy_main.close()
                    buy_show.clear()
                else:
                    print("> ไม่มีข้อมูลที่จะบันทึก <")
            elif confirm == "N":
                print("ยกเลิกการบันทึก")
            else :
                print("กรุณากรอก Y หรือ N เท่านั้น!!!")

    def View_Delete():
        list_count = []
        c = 0
        if len(buy_show) != 0:
            for x in buy_show:
                edit = x.split()
                c = c + 1
                list_count.append(str(c))
            edit_bc = ""
            while edit_bc != 0 and edit_bc != "N":
                while True:
                    try:
                        edit_bc = int(input("0 = ยกเลิก, กรอกลำดับรายการที่ต้องการลบ : "))
                        break
                    except ValueError:
                        print("กรุณากรอกลำดับเป็นตัวเลขเท่านั้น!!!")

                if edit_bc != 0:
                    if str(edit_bc) in list_count:
                        position = int(edit_bc)
                        pos = position - 1
                        list_delete = buy_show.pop(pos)
                        print("คุณได้ลบรายการที่ %d | %s" % (position, list_delete))
                        edit_bc = input("คุณต้องการลบข้อมูลต่อหรือไม่ (Y/N) : ").upper()
                        if edit_bc == "N":
                            break
                        elif edit_bc == "Y":
                            continue
                        else:
                            print("กรุณาเลือก Y หรือ N เท่านั้น!!!")
                    else:
                        print("ไม่มีลำดับสินค้านี้กรุณาลองอีกครั้ง")
                        while edit_bc != "N" and edit_bc != "Y":
                            edit_bc = input("คุณต้องการลบข้อมูลต่อหรือไม่ (Y/N) : ").upper()
                            if edit_bc == "N":
                                break
                            elif edit_bc == "Y":
                                continue
                            else:
                                print("กรุณาเลือก Y หรือ N เท่านั้น!!!")
        else:
            print("ไม่มีสินค้าให้ลบ")

    def View_Show():
        View_Set()
        print(" ", "-" * 83)
        print("|", "DemoPOS".center(82), "|")
        print("|", "  Sales number : ".rjust(17) + str(new_order), "Date : ".rjust(48) + str(dt_date), "|")
        print("|", "  seller : ".rjust(17) + show_username, "Time : ".rjust(49) + str(dt_time), "น.  ", "|")
        print("|", "-" * 82, "|")
        print("|", "NO".center(5), "|", "barcode".center(10), "|", "name".center(20), "|", "Price".center(10), "|",
              "Unit".center(10), "|", "Total".center(12), "|")
        print("|", "-" * 82, "|")

        if len(buy_show) == 0:
            print("|", "No Item".center(82), "|")
        count = 0
        global item_total
        item_total = 0
        global price_total
        price_total = 0
        for x in buy_show:
            show = x.split()
            count = count + 1
            print("|", str(count).center(5), "|", show[0].ljust(12), show[1].ljust(22), show[2].center(10),
                  show[3].center(12), show[4].rjust(14), "|")
            item_total = item_total + int(show[3])
            price_total = price_total + int(show[4])

        print(" ", "-" * 83)
        print("|", "Total : ".rjust(33) + str(item_total).rjust(5), "Item  ", "total :".rjust(23),
              str(price_total).rjust(12), "|")
        print(" ", "-" * 83)

    def Sell_main():
        barcode = input("กรุณากรอกรหัสสินค้า : ")
        def Check_AddProduct():
            if barcode != "":
                Product()
                check_bc=[]
                for x in product:
                    list_product = x.split()
                    check_bc.append(list_product[0])
                if barcode not in check_bc:
                    c_yn =""
                    while c_yn != "Y" and c_yn != "N":
                        c_yn = input("รหัสสินค้านี้ไม่มีอยู่ในระบบ คุณต้องการเพิ่มข้อมูลหรือไม่ (Y/N) : ").upper()
                        if c_yn == "Y":
                            file = open("product.txt", "a", encoding="utf=8")
                            add_name = input("กรุณากรอกชื่อสินค้า : ").replace(" ", "")
                            add_cost = int(input("กรุณากรอกราคาทุน : "))
                            add_price = int(input("กรุณากรอกราคาขาย : "))
                            file.write(barcode + " " + add_name + " " + str(add_cost) + " " + str(add_price) + "\n")
                            file.close()
                            print("> เพิ่มข้อมูลสำเร็จ <")
                        elif c_yn == "N":
                            print("ยกเลิกการเพิ่มข้อมูล")
                        else :
                            print("กรุณาเลือก Y และ N เท่านั้น")

        def AddToList():
            Product()
            new_product,new_barcode,new_name,new_price=[],[],[],[]
            for x in product:
                new_product = x.split()
                new_barcode.append(new_product[0])
                new_name.append(new_product[1])
                new_price.append(new_product[3])
            if barcode in new_barcode:
                index_pro = new_barcode.index(barcode)
                print("ชื่อสินค้า : " + new_name[index_pro])
                buy_num = int(input("กรุณากรอกจำนวนสินค้า : "))

                #เช็คว่าเคยเพิ่มสินค้าชิ้นนี้แล้วหรือยัง
                new_buy_show=[]
                list_old_barcode,list_old_name,list_old_price,list_old_buynum,list_old_buytotal=[],[],[],[],[]
                for x in buy_show:
                    new_buy_show = x.split()
                    list_old_barcode.append(new_buy_show[0])
                    list_old_name.append(new_buy_show[1])
                    list_old_price.append(new_buy_show[2])
                    list_old_buynum.append(new_buy_show[3])
                    list_old_buytotal.append(new_buy_show[4])
                if barcode in list_old_barcode:
                    position = list_old_barcode.index(barcode)
                    sum_num = int(list_old_buynum[position])+buy_num
                    old_total = int(list_old_buytotal[position])
                    new_total = int(list_old_price[position])*buy_num
                    sum_total = old_total+new_total
                    print("รหัสสินค้า ชื่อสินค้า ราคา จำนวน ราคารวม")
                    print("คุณได้เพิ่ม %s %s %s %d %.2f" % (barcode, new_name[index_pro], new_price[index_pro], buy_num, (int(new_price[index_pro]) * buy_num)))
                    buy_show[position]=("%s %s %s %s %s" % (barcode, new_name[index_pro], new_price[index_pro], str(sum_num),str(sum_total)))

                else:
                    print("รหัสสินค้า ชื่อสินค้า ราคา จำนวน ราคารวม")
                    print("คุณได้เพิ่ม %s %s %s %d %.2f" % (barcode, new_name[index_pro], new_price[index_pro], buy_num, (int(new_price[index_pro]) * buy_num)))
                    buy_show.append("%s %s %s %s %s" % (barcode, new_name[index_pro], new_price[index_pro], str(buy_num), str(int(new_price[index_pro]) * buy_num)))

            else:
                print("ไม่มีรหัสสินค้านี้ในระบบ")
        Check_AddProduct()
        AddToList()

    def View_Clear():
        sell_menu = ""
        while sell_menu != "N" and sell_menu != "Y":
            sell_menu = input("ยืนยันการล้างรายการขายทั้งหมดหรือไม่ (Y/N) : ").upper()
            if sell_menu == "Y":
                buy_show.clear()
                print("> ล้างข้อมูลเรียบร้อย <")
            elif sell_menu == "N":
                print("ยกเลิกการล้างข้อมูล")
            else:
                print("กรุณาเลือก Y หรือ N เท่านั้น!!!")

    def List_Product():
        Product()
        print("-" * 43)
        print("|","List Product".center(39),"|")
        print("-"*43)
        print("|","Barcode".ljust(10),"Product Name".ljust(20),"Price".ljust(7),"|")
        print("-" * 43)
        for x in product:
            sh = x.split()
            print("|",str(sh[0]).ljust(10), str(sh[1]).ljust(20), str(sh[3]).ljust(7),"|")
        print("-" * 43)

    buy_show = []
    sell_menu = ""
    while sell_menu != "B":
        if sell_menu != "L":
            View_Show()
        sell_menu = input(
            "S = บันทึก, D = ลบสินค้าในรายการ, C = ยกเลิก, B = กลับสู่หน้าหลัก, L = สินค้าทั้งหมด Enter = ซื้อสินค้าเพิ่มเติม : ").upper()
        if sell_menu == "S":
            print("> HOME/SELL/SAVE_SELL")
            View_Save()
        elif sell_menu == "D":
            print("> HOME/SELL/DELETE_LIST_SELL")
            View_Delete()
        elif sell_menu == "C":
            print("> HOME/SELL/CANCEL_SELL")
            View_Clear()
        elif sell_menu == "B":
            break
        elif sell_menu == "L":
            print("> HOME/SELL/LIST_PRODUCT")
            List_Product()
        elif sell_menu == "":
            Sell_main()
        else:
            print("กรุณาเลือกเมนูใหม่อีกครั้ง!")


#END PAGE SELL
#---------------------------------------------------------------------------------------------------------------
#START PAGE ORDER

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
            print("> HOME/ORDER/ORDER_DETAIL")
            Order_detail()
        elif order_menu == "D":
            print("> HOME/ORDER/DELETE")
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
            print("> HOME/ORDER/CLEAR")
            confirm = ""
            while confirm != "Y" and confirm != "N":
                confirm = input("คุณต้องการลบล้างรายการ ใช่หรือไม่ (Y/N) : " % str(order_menu)).upper()
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

#END PAGE ORDER
#---------------------------------------------------------------------------------------------------------------
#START PAGE PRODUCT

def Product():
    global product
    file = open("product.txt","r", encoding="utf-8")
    product = file.read().splitlines()
    file.close()

def Show_Product():
    Product()
    print("-" * 50)
    print("|", "List Product".center(47), "|")
    print("-" * 50)
    print("|", "Barcode".ljust(10), "Product Name".ljust(20), "Cost".ljust(7), "Price".ljust(7), "|")
    print("-" * 50)
    for x in product:
        sh = x.split()
        print("|", str(sh[0]).ljust(10), str(sh[1]).ljust(20), str(sh[2]).ljust(7), str(sh[3]).ljust(7), "|")
    print("-" * 50)

def Product_Menu():
    menu = ["เพิ่มสินค้า", "ลบสินค้า", "แก้ไขสินค้า", "ล้างข้อมูลสินค้า", "กลับสู่เมนูหลัก"]
    print("-" * 55)
    print("No.".center(6), "|", "Product Menu".ljust(20))
    print("-" * 55)
    count_menu = 0
    for x in menu:
        count_menu = count_menu + 1
        print(str(count_menu).center(6), "\t", str(x).ljust(20))
    print("-" * 55)

def Page_Product():
    Product()
    def Add_Product():
        print("> HOME/PRODUCT/ADD_PRODUCT")
        Show_Product()
        product_menu = ""
        while product_menu != "B" :
            product_menu = input("B = กลับ, Enter = เพิ้มข้อมูลสินค้า : ").upper()
            if product_menu != "B":
                add_pro_bc = input("กรุณากรอกรหัสสินค้า : ").upper()
                list_check_pro = []
                add_product=[]
                for x in product:
                    check_pro = x.split()
                    list_check_pro.append(check_pro[0])
                if add_pro_bc not in list_check_pro:
                    add_pro_name = input("กรุณากรอกชื่อสินค้า : ").replace(" ","")
                    add_pro_cost = input("กรุณากรอกราคาทุน : ")
                    add_pro_price = input("กรุณากรอกราคาขาย : ")
                    add_product.append("%s %s %s %s\n"%(add_pro_bc,add_pro_name,add_pro_cost,add_pro_price))
                    add_pro_file = open("product.txt","a", encoding="utf-8")
                    add_pro_file.write("%s %s %s %s\n"%(add_pro_bc,add_pro_name,add_pro_cost,add_pro_price))
                    print("ได้เพิ่ม %s %s %s %s เรียบร้อยแล้ว"%(add_pro_bc,add_pro_name,add_pro_cost,add_pro_price))
                    add_pro_file.close()
                    product_menu = input("Enter = ทำรายการต่อ, B = ย้อนกลับ, V = ดูข้อมูลสินค้า : ").upper()
                    if product_menu == "V":
                        Show_Product()
                else :
                    print("รหัสสินค้านี้ มีอยู่ในระบบแล้ว กรุณาลองใหม่อีกครั้ง!")
    def Delete_Product():
        print("> HOME/PRODUCT/DELETE_PRODUCT")
        Show_Product()
        product_menu=""
        list_product=[]
        copy_product = product
        while product_menu != "B" :
            product_menu = input("B = กลับ, Enter = ลบข้อมูลสินค้า : ").upper()
            if product_menu != "B":
                del_product = input("กรุณากรอกรหัสสินค้า : ")
                for x in product:
                    new_product = x.split()
                    list_product.append(new_product[0])
                if del_product in list_product:
                    pos = list_product.index(del_product)
                    del_detail = copy_product.pop(pos)
                    print("คุณได้ลบ %s"%del_detail)
                    file = open("product.txt","w",encoding="utf-8")
                    for x in copy_product:
                        data = x.split()
                        file.write("%s %s %s %s\n"%(data[0],data[1],data[2],data[3]))
                    print("บันทึกข้อมูลใหม่เรียบร้อย")
                    file.close()
                    product_menu = input("Enter = ทำรายการต่อ, B = ย้อนกลับ, V = ดูข้อมูลสินค้า : ").upper()
                    if product_menu == "V":
                        Show_Product()
                else:
                    print("ไม่มีรหัสสินค้านี้ในระบบ!")

    def Edit_Product():
        print("> HOME/PRODUCT/EDIT_PRODUCT")
        Show_Product()
        product_menu = ""
        list_edit_product=[]
        copy_product = product
        while product_menu != "B":
            product_menu = input("B = กลับ, Enter = แก้ไขข้อมูลสินค้า : ").upper()
            if product_menu != "B":
                for x in product:
                    new_product = x.split()
                    list_edit_product.append(new_product[0])
                product_menu = input("กรุณากรอกรหัสสินค้าที่ต้องการแก้ไข B = กลับสู่เมนู, V = ดูข้อมูลสินค้า : ").upper()
                if product_menu == "V":
                    Show_Product()
                if product_menu != "B" and product_menu != "V":
                    print("0 = รหัสสินค้า, 1 = ชื่อสินค้า, 2 = ราคาทุน, 3 = ราคาขาย")
                    if product_menu in list_edit_product:
                        pos = list_edit_product.index(product_menu)
                        edit_product = copy_product[pos].split()
                        select_pos = ""
                        print(edit_product)
                        while select_pos != "4":
                            select_pos = input("กรุณาเลือกช่องที่ต้องการแก้ไข (0-3) หรือ 4 = กลับหน้าหลัก : ")
                            if select_pos == "0":
                                edit_product[0] = input("กรุณากรอกรหัสสินค้า : ")
                            elif select_pos == "1":
                                edit_product[1] = input("กรุณากรอกชื่อสินค้า : ")
                            elif select_pos == "2":
                                edit_product[2] = input("กรุณากรอกราคาทุน : ")
                            elif select_pos == "3":
                                edit_product[3] = input("กรุณากรอกราคาขาย : ")
                            print("คุณแก้ไขเปน : %s %s %s %s" %(edit_product[0], edit_product[1], edit_product[2], edit_product[3]))
                        copy_product[pos] = edit_product[0]+" "+edit_product[1]+" "+edit_product[2]+" "+edit_product[3]
                        file = open("product.txt","w",encoding="utf-8")
                        for x in copy_product:
                            add_edit_pro = x.split()
                            file.write("%s\n"%(x))
                        file.close()
                        product_menu = input("Enter = ทำรายการต่อ, B = ย้อนกลับ, V = ดูข้อมูลสินค้า : ").upper()
                        if product_menu == "V":
                            Show_Product()
                    else:
                        print("ไม่มีข้อมูลสินค้านี้ในอยู่ในระบบ")

    def Clear_Product():
        print("> HOME/PRODUCT/DELETA_ALL_PRODUCT")
        Show_Product()
        confirm = ""
        product_menu = ""
        while confirm != "B" and product_menu != "B":
            product_menu = input("B = กลับ, Enter = ล้างข้อมูลสินค้า : ").upper()
            if product_menu != "B":
                confirm = input("คุณต้องการล้างข้อมูลหรือไม่ (Y/N) B = กลับสู่หน้าหลัก : ").upper()
                if confirm == "Y":
                    file = open("product.txt","w")
                    file.write("")
                    file.close()
                    print("ล้างข้อมูลสำเร็จ")
                else:
                    print("ยกเลิกการล้างข้อมูล")

    pro_menu = ""
    while pro_menu != "5":
        Product_Menu()
        pro_menu = input("กรุณาเลือกเมนู (1-5) : ")
        print("-" * 55)
        if pro_menu == "1":
            Add_Product()
        elif pro_menu == "2":
            Delete_Product()
        elif pro_menu == "3":
            Edit_Product()
        elif pro_menu == "4":
            Clear_Product()
        elif pro_menu == "5":
            break
        else:
            print("กรุณาเลือกเมนุ (1-5) เท่านั้น!!!")


#END PAGE PRODUCT
#---------------------------------------------------------------------------------------------------------------
#START PAGE ACCOUNT

def Account():
    global account
    file = open("account.txt","r", encoding="utf-8")
    account = file.read().splitlines()
    file.close()



def Page_Account():
    def Show_Account():
        Account()
        account_no = 0
        print("-" * 55)
        print("|","Account".center(51),"|")
        print("-" * 55)
        print("|", "NO.".center(5), "|", "Username".center(20), "|", "Password".center(20), "|")
        print("-" * 55)
        for x in account:
            account_no = account_no+1
            new_account = x.split()
            print("|",str(account_no).center(5),"|",str(new_account[0]).ljust(20), "|",str(new_account[1]).ljust(20),"|")
        print("-" * 55)

    def Account_menu():
        list_menu = ["เพิ่มข้อมูลผู้ใช้","ลบข้อมูลผู้ใช้","แก้ไขข้อมูลผู้ใช้","ล้างข้อมูลผู้ใช้","กลับสู่หน้าหลัก"]
        print("-"*55)
        print("No.".center(6),"|","Account Menu".ljust(20))
        print("-" * 55)
        count_menu=0
        for x in list_menu:
            count_menu = count_menu+1
            print(str(count_menu).center(6),"\t",str(x).ljust(20))
        print("-" * 55)


    def Add_Account():
        print("> HOME/ACCOUNT/ADD_ACCOUNT")
        print("-" * 55)
        print("ADD ACCOUNT".center(51))
        print("-" * 55)
        ac_menu = ""
        while ac_menu != "B":
            ac_menu = input("B = กลับ, Enter = เพิ่มข้อมูลผู้ใช้ : ").upper()
            if ac_menu != "B":
                add_username = ""
                add_username = input("กรุณากรอกชื่อผู้ใช่งาน : ").lower()
                Account()
                new_username,new_password = [],[]
                for x in account:
                    new_account = x.split()
                    new_username.append(new_account[0])
                    new_password.append(new_account[1])
                if add_username not in new_username:
                    add_password = "0"
                    confirm_password = "1"
                    while add_password != confirm_password:
                        add_password = input("กรุณากรอกรหัสผ่าน : ").lower()
                        confirm_password = input("กรุณายืนยันรหัสผ่าน : ").lower()
                        if add_password == confirm_password:
                            add_account = open("account.txt", "a", encoding="utf-8")
                            add_account.write("%s %s\n"%(add_username,add_password))
                            add_account.close()
                            print("-" * 55)
                            print("> เพิ่มชื่อผู้ใช้ : %s เข้าสู่ระบบเรียบร้อยแล้ว"%add_username)
                            print("-" * 55)
                        else :
                            print("-" * 55)
                            print("รหัสผ่านไม่ตรงกันกรุณากรอกรหัสผ่านใหม่อีกครั้ง!!!")
                            print("-" * 55)
                else:
                    print("-" * 55)
                    print("ชื่อผู้ใช้งานนี้ภูกใช้ไปแล้ว!!!")
                    print("-" * 55)
                Show_Account()

    def Delete_Account():
        print("> HOME/ACCOUNT/Delete_Account")
        ac_menu = ""
        while ac_menu != "B":
            Show_Account()
            ac_menu = input("B = กลับ, Enter = ลบข้อมูลผู้ใช้ : ").upper()
            if ac_menu != "B":
                del_account = input("กรุณากรอกชื่อผู้ใช้ที่ต้องการลบ : ").lower()
                Account()
                new_username,new_password = [],[]
                for x in account:
                    new_account = x.split()
                    new_username.append(new_account[0])
                    new_password.append(new_account[1])
                if del_account in new_username:
                    pos = new_username.index(del_account)
                    confirm = ""
                    while confirm != "Y" and confirm != "N":
                        confirm = input("คุณต้องการลบชื่อผู้ใช้ : %s นี้ใช่หรือไม่ (Y/N) : " % str(del_account)).upper()
                        if confirm == "Y":
                            account.pop(pos)
                            file = open("account.txt","w")
                            for x in account:
                                new_account = x.split()
                                file.write("%s %s\n"%(new_account[0], new_account[1]))
                            file.close()
                        elif confirm == "N":
                            print("ยกเลิกการลบข้อมูล")
                        else:
                            print("กรุณากด Y หรือ N เท่านั้น!!!")
                else :
                    print("ไม่มีชื่อผู้ใช้นี้อยู่ในระบบ!!!")

    def Clear_Account():
        print("> HOME/ACCOUNT/DELETE_ALL_ACCOUNT")
        ac_menu = ""
        while ac_menu != "B":
            Show_Account()
            ac_menu = input("B = กลับ, Enter = ลบข้อมูลผู้ใช้ทั้งหมด : ").upper()
            if ac_menu != "B":
                Account()
                confirm = ""
                while confirm != "Y" and confirm != "N":
                    confirm = input("คุณต้องการลบชื่อผู้ใช้ทั้งหมด ใช่หรือไม่ (Y/N) : ").upper()
                    if confirm == "Y":
                        file = open("account.txt", "w")
                        file.write("admin 1234\n")
                        file.close()
                    elif confirm == "N":
                        print("ยกเลิกการลบข้อมูล")
                    else:
                        print("กรุณากด Y หรือ N เท่านั้น!!!")

    def Edit_Account():
        print("> HOME/ACCOUNT/EDIT_ACCOUNT")
        ac_menu=""
        while ac_menu != "B":
            Show_Account()
            ac_menu = input("B = กลับ, Enter = แก้ไขข้อมูลผู้ใช้ : ").upper()
            if ac_menu != "B":
                ac_menu = input("กรุณาเลือกเชื่อผู้ใช้ที่ต้องการแก้ไข : ")
                Account()
                list_username,list_password = [],[]
                for x in account:
                    new_account = x.split()
                    list_username.append(new_account[0])
                    list_password.append(new_account[1])
                if ac_menu in list_username:
                    pos = list_username.index(ac_menu)
                    print("-" * 55)
                    print("|", "NO.".center(5), "|", "Username".center(20), "|", "Password".center(20), "|")
                    print("-" * 55)
                    for x in account:
                        new_account = x.split()
                        if ac_menu == new_account[0]:
                            print("|", str(1).center(5), "|", str(list_username[pos]).ljust(20), "|",
                                  str(list_password[pos]).ljust(20), "|")
                    print("-" * 55)
                    ac_menu = ""
                    while ac_menu != "B" and ac_menu != "C" and ac_menu != "S":
                        ac_menu = input("1.แก้ไขชื่อผู้ใช้งาน, 2.แก้ไขรหัสผ่าน, S = บันทึก, C = ยกเลิก B = กลับ :").upper()
                        if ac_menu == "1":
                            old_username = list_username[pos]
                            list_username[pos] = input("กรุณากรอกชื่อผู้ใช้ที่ต้องการแก้ไข : ").lower()
                            print("คุณเปลี่ยนจาก %s เป็น %s"%(str(old_username),str(list_username[pos])))
                        elif ac_menu == "2":
                            old_password = list_password[pos]
                            list_password[pos] = input("กรุณากรอกรหัสผ่านที่ต้องการแก้ไข : ").lower()
                            print("คุณเปลี่ยนจาก %s เป็น %s" % (str(old_password), str(list_password[pos])))
                        elif ac_menu == "S":
                            Account()
                            account[pos] = str(list_username[pos])+" "+str(list_password[pos])
                            file = open("account.txt", "w")
                            for x in account:
                                file.write("%s\n"%(x))
                            file.close()
                            print("บันทึกข้อมูลผู้ใช้งานเรียบร้อย")
                        elif ac_menu == "C":
                            print("ยกเลิกการแก้ไข")
                        elif ac_menu == "B":
                            break
                        else:
                            print("กรุณาเลือกเมนู 1, 2, S, C, B เท่านั้น!!!")
                else:
                    print("ไม่มีชื่อผู้ใช้นี้อยู่ในระบบ!!!")


    ac_menu = ""
    while ac_menu != "5":
        Account_menu()
        ac_menu = input("กรุณาเลือกเมนู (1-5) : ")
        print("-" * 55)
        if ac_menu == "1":
            Add_Account()
        elif ac_menu == "2":
            Delete_Account()
        elif ac_menu == "3":
            Edit_Account()
        elif ac_menu == "4":
            Clear_Account()
        elif ac_menu == "5":
            break
        else :
            print("กรุณาเลือกเมนุ (1-5) เท่านั้น!!!")






#END PAGE ACCOUNT
#---------------------------------------------------------------------------------------------------------------
#START PAGE MENU

def Account():
    global account
    file = open("account.txt", "r", encoding="utf-8")
    account = file.read().splitlines()
    file.close()




def Menu():
    print("> HOME")
    menu = ["หน้าขายสินค้า","หน้าแสดงยอดการขายสินค้า","หน้าจัดการสินค้า","หน้าจัดการชื่อผู้ใช้","ล็อคเอาท์","ออกโปรแกรม"]
    print("-"*55)
    print("No.".center(6),"|","Home Menu".ljust(20))
    print("-" * 55)
    count_menu=0
    for x in menu:
        count_menu = count_menu+1
        print(str(count_menu).center(6),"\t",str(x).ljust(20))
    print("-" * 55)


Account()
new_user, new_pass = [], []
for x in account:
    new_account = x.split()
    new_user.append(new_account[0])
    new_pass.append(new_account[1])


login = ""
username = ""
status = ""
while username not in new_user or status == "logout":
    print("-" * 55)
    print("|", "LOGIN".center(52), "|")
    print("-" * 55)
    print("|", "USERNAME(DEFAULT) : admin".ljust(24), "|", "PASSWORD(DEFAULT) : 1234".rjust(24), "|")
    print("-" * 55)
    username = input("USERNAME : ".rjust(18)).lower()
    if username in new_user:
        password = ""
        while password not in new_pass:
            password = input("PASSWORD : ".rjust(18)).lower()
            if password in new_pass:
                status == "login"
                show_username = username
                home_menu = ""
                while home_menu != "6":
                    Menu()
                    home_menu = input("กรุณาเลือกเมนู (1-5) : ")
                    print("-" * 55)
                    if home_menu == "1":
                        print("> HOME/SELL")
                        Page_sell()
                    elif home_menu == "2":
                        print("> HOME/ORDER")
                        Show_MainOrder()
                    elif home_menu == "3":
                        print("> HOME/PRODUCT")
                        Page_Product()
                    elif home_menu == "4":
                        print("> HOME/ACCOUNT")
                        Page_Account()
                    elif home_menu == "5":
                        status = "logout"
                        break
                    elif home_menu == "6":
                        exit()
                    else:
                        print("กรุณาเลือกเมนุ (1-6) เท่านั้น!!!")
            else:
                print("รหัสผ่านไม่ถูกต้องกรุณาลองใหม่อีกครั้ง!!!".center(78))
    else:
        print("ชื่อผู้ใช้งานไม่ถูกต้องกรุณาลองใหม่อีกครั้ง!!!".center(82))
print("-" * 55)