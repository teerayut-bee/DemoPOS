
for x in range(256):
    print("\33[38;5;"+str(x)+"m" + str(x) + "\33[0m")

for x in range(256):
    print("\33[48;5;"+str(x)+"m" + str(x) + "\33[0m")


    def Orange(text):
        return "\33[38;5;208m" + text + "\33[0m"


    def Red(text):
        return "\33[38;5;1m" + text + "\33[0m"


    def Pink(text):
        return "\33[38;5;162m" + text + "\33[0m"


    def White(text):
        return "\33[38;5;253m" + text + "\33[0m"


    def Yellow(text):
        return "\33[38;5;220m" + text + "\33[0m"


    def Blue(text):
        return "\33[38;5;38m" + text + "\33[0m"


    def Green(text):
        return "\33[38;5;47m" + text + "\33[0m"