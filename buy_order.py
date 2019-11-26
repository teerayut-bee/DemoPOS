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

def Show_MainOrder():
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

Show_MainOrder()