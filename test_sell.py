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
    Sell_menu()
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