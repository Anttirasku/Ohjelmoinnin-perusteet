pisteet=int(input("Anna pisteesi: "))
arvosana0=[0,1]
arvosana1=[2,3]
arvosana2=[4,5]
arvosana3=[6,7]
arvosana4=[8,9]
arvosana5=[10,11,12]
if pisteet in arvosana0:
    print("Arvosana: 0")
elif pisteet in arvosana1:
    print("Arvosana: 1")
elif pisteet in arvosana2:
    print("Arvosana: 2")
elif pisteet in arvosana3:
    print("Arvosana: 3")
elif pisteet in arvosana4:
    print("Arvosana: 4")
elif pisteet in arvosana5:
    print("Arvosana: 5")
elif pisteet != [arvosana0,arvosana1,arvosana2,arvosana3,arvosana4,arvosana5]:
    print("Tarkista syötteesi ja aja ohjelma uudelleen.")