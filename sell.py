buy_show = []
bc = ""

def Product():
    global product
    file = open("product.txt","r", encoding="utf-8")
    product = file.read().splitlines()
    file.close()


def Buy_main():
    global buy_main
    file = open("buy_main.txt", "r", encoding="utf-8")
    buy_main = file.read().splitlines()
    file.close()

def Buy_menu():
    global buy_menu
    buy_menu = ""
    while buy_menu != "B":
        buy_menu = input("V = แสดงข้อมูลการซื้อ, B = กลับสู่เมนูหลัก, S = แสดงสินค้าทั้งหมด, Enter = ทำรายการต่อ : ").upper()
        if buy_menu == "V":
            Buy_view()
        elif buy_menu == "S":
            Buy_Show()
        elif buy_menu == "":
            bc = input("กรุณากรอกรหัสสินค้า : ")
            Buy_CheckProduct()
            Buy_AddList()


def Buy_CheckProduct():
    Product()
    check_bc=[]
    for x in product:
        list_product = x.split()
        check_bc.append(list_product[0])
    if bc not in check_bc:
        c_yn = input("รหัสสินค้านี้ไม่มีอยู่ในระบบ คุณต้องการเพิ่มข้อมูลหรือไม่ Y = Yes : ").upper()
        if c_yn == "Y":
            file = open("product.txt", "a", encoding="utf=8")
            add_bc = bc
            add_name = input("กรุณากรอกชื่อสินค้า : ").replace(" ", "")
            add_cost = int(input("กรุณากรอกราคาทุน : "))
            add_price = int(input("กรุณากรอกราคาขาย : "))
            file.write(add_bc + " " + add_name + " " + str(add_cost) + " " + str(add_price) + "\n")
            file.close()
            print("> เพิ่มข้อมูลสำเร็จ <")

def Buy_AddList():
    check_bc2 = []
    list_product2 = []
    Product()
    buy_name=[]
    buy_price=[]
    for x in product:
        list_product2 = x.split()
        check_bc2.append(list_product2[0])
        buy_name.append(list_product2[1])
        buy_price.append(list_product2[3])
    if bc in check_bc2:
        index_pro = check_bc2.index(bc)
        print("ชื่อสินค้า : "+buy_name[index_pro])
        buy_num = int(input("กรุณากรอกจำนวนสินค้า : "))
        print("รหัสสินค้า ชื่อสินค้า ราคา จำนวน ราคารวม")
        print("คุณได้เพิ่ม %s %s %s %d %.2f"%(bc,buy_name[index_pro],buy_price[index_pro],buy_num,(int(buy_price[index_pro])*buy_num)))
        buy_show.append("%s %s %s %s %s"%(bc,buy_name[index_pro],buy_price[index_pro],str(buy_num),str(int(buy_price[index_pro])*buy_num)))
    else:
        print("ไม่มีรหัสสินค้านี้ในระบบ")


def Buy_Show():
    Product()
    print("รหัสสินค้า ชื่อสินค้า ราคา")
    for x in product:
        show = x.split()
        print("%s %s %s" % (show[0], show[1], show[3]))

def Buy_view():
    from datetime import datetime
    now = datetime.now()
    dt_date = now.strftime("%d/%m/%Y")
    dt_time = now.strftime("%H:%M")

    if len(buy_main) == 0:
        new_order = "N" + "1".rjust(5, "0")
    else:
        for x in buy_main:
            list_order = x.split()
            last_order = str(list_order[0])
        old_order = int(last_order[1:6])
        new_order = "N" + str(old_order + 1).rjust(5, "0")

    print(" ", "-" * 83)
    print("|", "DemoPOS".center(82), "|")
    print("|", "  Sales number : ".rjust(17) + str(new_order), "Date : ".rjust(48) + str(dt_date), "|")
    print("|", "  seller : ".rjust(17) + "Admin", "Time : ".rjust(49) + str(dt_time), "น.  ", "|")
    print("|", "-" * 82, "|")
    print("|", "NO".center(5), "|", "barcode".center(10), "|", "name".center(20), "|", "Price".center(10), "|",
              "Unit".center(10), "|", "Total".center(12), "|")
    print("|", "-" * 82, "|")

    if len(buy_show) == 0:
        print("|", "No Item".center(82), "|")

    count = 0
    item_total = 0
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

    buy_menu = input("S = บันทึก, E = ลบสินค้าในรายการ, C = ยกเลิก, B = กลับสู่หน้าหลัก, Enter = ซื้อสินค้าเพิ่มเติม : ").upper()
    if buy_menu == "S":
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
    elif buy_menu == "E":
        index_edit_bc = 0
        count = []
        c = 0
        if len(buy_show) != 0:
            for x in buy_show:
                edit = x.split()
                c = c + 1
                count.append(str(c))
            edit_bc = ""
            while edit_bc != "E":
                edit_bc = input("กรุณากรอกลำดับรายการที่ต้องการลบ หรือ E = Exit : ").upper()
                if edit_bc != "E":
                    if edit_bc in count:
                        position = int(edit_bc)
                        pos = position - 1
                        list_delete = buy_show.pop(pos)
                        print("คุณได้ลบรายการที่ %d | %s" % (position, list_delete))
                        edit_bc = "E"
                    else:
                        print("ไม่มีลำดับสินค้านี้นี้กรุณาลองอีกครั้ง")
        else:
            print("ไม่มีสินค้าให้แก้ไข")
    elif buy_menu == "C":
        confirm = input("ยืนยันการลบ (Y/N) : ").upper()
        if confirm == "Y":
            buy_show.clear()
            print("> ล้างข้อมูลเรียบร้อย <")

Buy_menu()