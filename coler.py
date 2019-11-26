
for x in range(256):
    print("\33[38;5;"+str(x)+"m" + str(x) + "\33[0m")

for x in range(256):
    print("\33[48;5;"+str(x)+"m" + str(x) + "\33[0m")