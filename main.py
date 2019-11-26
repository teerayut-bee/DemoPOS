def Product():
    global product
    file = open("product.txt","r", encoding="utf-8")
    product = file.read().splitlines()
    file.close()

buy_show = []

def Page_buy():
    check_bc=[]
    buy_name = []
    buy = []
    buy_detail = []
    buy_price=[]
    index_pro=0

    Product();
    buy_menu = ""
    bc = ""
    while buy_menu != "B" or bc != "B":
        buy_num = 0
        bc = input("กรุณากรอกรหัสสินค้า หรือกด V = แสดงข้อมูลสินค้า หรือ B = กลับสู่เมนูหลัก หรือ S = แสดงสินค้าทั้งหมด: ").upper()
        if bc == "S":
            print("รหัสสินค้า ชื่อสินค้า ราคา")
            for x in product:
                sh = x.split()
                print("%s %s %s"%(sh[0],sh[1],sh[3]))
            bc = input("กรุณากรอกรหัสสินค้า หรือกด V = แสดงข้อมูลสินค้า หรือ B = กลับสู่เมนูหลัก หรือ S = แสดงสินค้าทั้งหมด: ").upper()

        if bc != "V" and bc != "B":
            for x in product :
                list_product = x.split()
                check_bc.append(list_product[0])
            if bc not in check_bc:
                c_yn = input("รหัสสินค้านี้ไม่มีอยู่ในระบบ คุณต้องการเพิ่มข้อมูลหรือไม่ Y = Yes : ").upper()
                if c_yn == "Y":
                    file = open("product.txt","a", encoding="utf=8")
                    add_bc = bc
                    add_name = input("กรุณากรอกชื่อสินค้า : ").replace(" ","")
                    add_cost = int(input("กรุณากรอกราคาทุน : "))
                    add_price = int(input("กรุณากรอกราคาขาย : "))
                    file.write("\n"+add_bc+" "+add_name+" "+str(add_cost)+" "+str(add_price))
                    file.close()
                    print("> เพิ่มข้อมูลสำเร็จ <")

            check_bc2 = []
            list_product2 = []
            file2 = open("product.txt", "r", encoding="utf-8")
            product2 = file2.read().splitlines()
            file2.close()
            buy_name=[]
            buy_price=[]
            for x in product2:
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
        elif bc == "V" :
            from datetime import datetime

            now = datetime.now()
            dt_date = now.strftime("%d/%m/%Y")
            dt_time = now.strftime("%H:%M")


            def Buy_main():
                global buy_main
                file = open("buy_main.txt", "r", encoding="utf-8")
                buy_main = file.read().splitlines()
                file.close()


            Buy_main()
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

            if len(buy_show) == 0 :
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
                        f_buy_detail.write("%s %s %s %s %s %s\n"%(new_order,ex[0],ex[1],ex[2],ex[3],ex[4]))
                    f_buy_main.write("%s %s %s %s %s %s\n" % (new_order, str(dt_date), str(dt_time), "admin", str(item_total), str(price_total)))
                    print("> บันทึกสินค้าเรียบร้อย <")
                    f_buy_detail.close()
                    f_buy_main.close()
                    buy_show.clear()
                else :
                    print("> ไม่มีข้อมูลที่จะบันทึก <")
            elif buy_menu == "E":
                index_edit_bc = 0
                count=[]
                c = 0
                if len(buy_show) != 0:
                    for x in buy_show:
                        edit = x.split()
                        c = c+1
                        count.append(str(c))
                    edit_bc =""
                    while edit_bc != "E":
                        edit_bc = input("กรุณากรอกลำดับรายการที่ต้องการลบ หรือ E = Exit : ").upper()
                        if edit_bc != "E":
                            if edit_bc in count:
                                position = int(edit_bc)
                                pos = position-1
                                list_delete = buy_show.pop(pos)
                                print("คุณได้ลบรายการที่ %d | %s"%(position,list_delete))
                                edit_bc = "E"
                            else :
                                print("ไม่มีลำดับสินค้านี้นี้กรุณาลองอีกครั้ง")
                else :
                    print("ไม่มีสินค้าให้แก้ไข")
            elif buy_menu == "C":
                confirm = input("ยืนยันการลบ (Y/N) : ").upper()
                if confirm == "Y":
                    buy_show.clear()
                    print("> ล้างข้อมูลเรียบร้อย <")
        if buy_menu == "B":
            bc = "B"
        elif bc == "B":
            buy_menu = "B"



main_menu = ""

while main_menu != 5:
    main_menu = int(input(">>>Manu<<<\n1.หน้าขายสินค้า\n2.หน้าแสดงยอดการขายสินค้า\n3.หน้าจัดการสินค้า\n4.หน้าจัดการชื่อผู้ใช้\n5.ออกโปรแกรม\n> กรุณาเลือกเมนูที่ท่านต้องการ : "))

    if main_menu == 1:
        Page_buy()
    elif main_menu == 2:
        print("หน้าแสดงยอดการขายสินค้า")
    elif main_menu == 3:
        print("หน้าจัดการสินค้า")
    elif main_menu == 4:
        print("หน้าจัดการชื่อผู้ใช้")
print("ออกจากระบบ")
