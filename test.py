def Product():
    global product
    file = open("product.txt","r", encoding="utf-8")
    product = file.read().splitlines()
    file.close()

Product()
pro_menu = ""
while pro_menu != "5" :
    pro_menu = input("***เมนูย่อย***\n1.เพิ่มสินค้า\n2.ลบสินค้า\n3.แก้ไขสินค้า\n4.ล้างข้อมูลสินค้า\n5.กลับสู่เมนูหลัก\nกรุณาเลือกเมนู : ").upper()
    if pro_menu == "1" :
        product_menu = ""
        product_menu = input("Enter = ทำรายการต่อ, B = ย้อนกลับ, V = ดูข้อมูลสินค้า : ").upper()
        if product_menu == "V":
            print("รหัสสินค้า ชื่อสินค้า ทุน ราคา")
            for x in product:
                sh = x.split()
                print("%s %s %s %s" % (sh[0], sh[1], sh[2], sh[3]))
        while product_menu != "B" :
            add_pro_bc = input("กรุณากรอกรหัสสินค้า : ").upper()
            list_check_pro = []
            add_product=[]
            Product()
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
                    Product()
                    print("รหัสสินค้า ชื่อสินค้า ทุน ราคา")
                    for x in product:
                        sh = x.split()
                        print("%s %s %s %s" % (sh[0], sh[1], sh[2], sh[3]))
            else :
                print("รหัสสินค้านี้ มีอยู่ในระบบแล้ว กรุณาลองใหม่อีกครั้ง!")
                product_menu = input("Enter = ทำรายการต่อ, B = ย้อนกลับ, V = ดูข้อมูลสินค้า : ").upper()
                if product_menu == "V":
                    print("รหัสสินค้า ชื่อสินค้า ทุน ราคา")
                    for x in product:
                        sh = x.split()
                        print("%s %s %s %s" % (sh[0], sh[1], sh[2], sh[3]))
    elif pro_menu == "2":
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
                    print("รหัสสินค้า ชื่อสินค้า ทุน ราคา")
                    for x in product:
                        sh = x.split()
                        print("%s %s %s %s" % (sh[0], sh[1], sh[2], sh[3]))
            else:
                print("ไม่มีรหัสสินค้านี้ในระบบ!")

    elif pro_menu == "3":
        product_menu = ""
        list_edit_product=[]
        copy_product = product
        while product_menu != "B":
            for x in product:
                new_product = x.split()
                list_edit_product.append(new_product[0])
            product_menu = input("กรุณากรอกรหัสสินค้าที่ต้องการแก้ไข B = กลับสู่เมนู, V = ดูข้อมูลสินค้า : ").upper()
            if product_menu == "V":
                print("รหัสสินค้า ชื่อสินค้า ทุน ราคา")
                for x in product:
                    sh = x.split()
                    print("%s %s %s %s" % (sh[0], sh[1], sh[2], sh[3]))
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
                        print("รหัสสินค้า ชื่อสินค้า ทุน ราคา")
                        for x in product:
                            sh = x.split()
                            print("%s %s %s %s" % (sh[0], sh[1], sh[2], sh[3]))
                else:
                    print("ไม่มีข้อมูลสินค้านี้ในอยู่ในระบบ")

    elif pro_menu == "4":
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





