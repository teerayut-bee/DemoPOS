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
        print("> HOME/ACCOUNT")
        list_menu = ["เพิ่มข้อมูลผู้ใช้","ลบข้อมูลผู้ใช้","แก้ไขข้อมูลผู้ใช้","ล้างข้อมูลผู้ใช้","กลับสู่หน้าหลัก"]
        print("-"*55)
        print("No.".center(6),"|","Menu".center(20))
        print("-" * 55)
        count_menu=0
        for x in list_menu:
            count_menu = count_menu+1
            print(str(count_menu).center(6),"\t",str(x).ljust(20))
        print("-" * 55)


    def Add_Account():
        print("> HOME/ACCOUNT/ADD ACCOUNT")
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
                        print("-" * 30)
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
        print("> HOME/ACCOUNT/Delete Account")
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
        print("> HOME/ACCOUNT/DELETE ALL")
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
        print("> HOME/ACCOUNT/EDIT Account")
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





Page_Account()