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
                    Sell_View()
                else:
                    print("รหัสสินค้า ชื่อสินค้า ราคา จำนวน ราคารวม")
                    print("คุณได้เพิ่ม %s %s %s %d %.2f" % (barcode, new_name[index_pro], new_price[index_pro], buy_num, (int(new_price[index_pro]) * buy_num)))
                    buy_show.append("%s %s %s %s %s" % (barcode, new_name[index_pro], new_price[index_pro], str(buy_num), str(int(new_price[index_pro]) * buy_num)))
                    Sell_View()
            else:
                print("ไม่มีรหัสสินค้านี้ในระบบ")
        Check_AddProduct()
        AddToList()

    def Sell_View():
        def View_Set():
            from datetime import datetime
            global dt_date,dt_time,new_order
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

        def View_Show():
            View_Set()
            print(" ", "-" * 83)
            print("|", "DemoPOS".center(82), "|")
            print("|", "  Sales number : ".rjust(17) + str(new_order), "Date : ".rjust(48) + str(dt_date), "|")
            print("|", "  seller : ".rjust(17) + "Admin", "Time : ".rjust(49) + str(dt_time), "น.  ", "|")
            print("|", "-" * 82, "|")
            print("|", "NO".center(5), "|", "barcode".center(10), "|", "name".center(20), "|", "Price".center(10), "|","Unit".center(10), "|", "Total".center(12), "|")
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

        def View_Save():
            if len(buy_show) != 0:
                f_buy_main = open("buy_main.txt", "a", encoding="utf-8")
                f_buy_detail = open("buy_detail.txt", "a", encoding="utf-8")
                for x in buy_show:
                    ex = x.split()
                    f_buy_detail.write("%s %s %s %s %s %s\n" % (new_order, ex[0], ex[1], ex[2], ex[3], ex[4]))
                f_buy_main.write("%s %s %s %s %s %s\n" % (
                new_order, str(dt_date), str(dt_time), "admin", str(item_total), str(price_total)))
                print("> บันทึกสินค้าเรียบร้อย <")
                f_buy_detail.close()
                f_buy_main.close()
                buy_show.clear()
            else:
                print("> ไม่มีข้อมูลที่จะบันทึก <")

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

                    if edit_bc != 0 :
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


        sell_menu =""
        while sell_menu != "B":
            View_Show()
            sell_menu = input("S = บันทึก, D = ลบสินค้าในรายการ, C = ยกเลิก, B = กลับสู่หน้าหลัก, L = สินค้าทั้งหมด Enter = ซื้อสินค้าเพิ่มเติม : ").upper()
            if sell_menu == "S":
                View_Save()
            elif sell_menu == "D":
                View_Delete()
            elif sell_menu == "C":
                View_Clear()
            elif sell_menu == "B":
                break
            elif sell_menu == "L":
                List_Product()
            elif sell_menu == "":
                Sell_main()
            else:
                print("กรุณาเลือกเมนูใหม่อีกครั้ง!")

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



    buy_show=[]
    sell_menu = ""
    while sell_menu != "B":
        sell_menu = input("V = แสดงข้อมูลการซื้อ, B = กลับสู่เมนูหลัก, S = แสดงสินค้าทั้งหมด, Enter = ทำรายการต่อ : ").upper()
        if sell_menu == "V":
            Sell_View()
        elif sell_menu == "S":
            List_Product()
        elif sell_menu == "":
            Sell_main()
        elif sell_menu == "B" :
            break
        else:
            print("Try Again")
    print("Exit")

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
def Page_Product():
    Product()
    pro_menu = ""
    while pro_menu != "5" :
        pro_menu = input("***เมนูย่อย***\n1.เพิ่มสินค้า\n2.ลบสินค้า\n3.แก้ไขสินค้า\n4.ล้างข้อมูลสินค้า\n5.กลับสู่เมนูหลัก\nกรุณาเลือกเมนู : ").upper()
        if pro_menu == "1" :
            Show_Product()
            product_menu = ""
            while product_menu != "B" :
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
        elif pro_menu == "2":
            Show_Product()
            product_menu=""
            list_product=[]
            copy_product = product
            while product_menu != "B" :
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

        elif pro_menu == "3":
            Show_Product()
            product_menu = ""
            list_edit_product=[]
            copy_product = product
            while product_menu != "B":
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

        elif pro_menu == "4":
            Show_Product()
            confirm = ""
            while confirm != "B":
                confirm = input("คุณต้องการล้างข้อมูลหรือไม่ (Y/N) B = กลับสู่หน้าหลัก : ").upper()
                if confirm == "Y":
                    file = open("product.txt","w")
                    file.write("")
                    file.close()
                    print("ล้างข้อมูลสำเร็จ")
                else:
                    print("ยกเลิกการล้างข้อมูล")


#END PAGE ORDER
#---------------------------------------------------------------------------------------------------------------
#START PAGE PRODUCT


main_menu = ""

while main_menu != 5:
    main_menu = int(input(">>>Manu<<<\n1.หน้าขายสินค้า\n2.หน้าแสดงยอดการขายสินค้า\n3.หน้าจัดการสินค้า\n4.หน้าจัดการชื่อผู้ใช้\n5.ออกโปรแกรม\n> กรุณาเลือกเมนูที่ท่านต้องการ : "))

    if main_menu == 1:
        Page_sell()
    elif main_menu == 2:
        Show_MainOrder()
    elif main_menu == 3:
        Page_Product()
    elif main_menu == 4:
        print("หน้าจัดการชื่อผู้ใช้")
print("ออกจากระบบ")
