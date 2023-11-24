rekisterit = []
while True:
    rekisteri= input("Syötä rekisterinumero: ")
    if rekisteri == "":
        break
    rekisterit.append(rekisteri)
rekisterit.sort()
print(rekisterit)