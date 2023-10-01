def neliö(luku):
        return luku ** 2

while True:
    luku = int(input("Anna numero väliltä 1-10: "))
    if luku==0:
        break
    elif 1<= luku <=10:
        for toistokerrat in range(1,luku+1):
            nelioarvo=neliö(toistokerrat)
            print(f"Luvun {toistokerrat} neliö on {nelioarvo}")
    else:
         break