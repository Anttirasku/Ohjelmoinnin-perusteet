oppilaita = []
maara = 0
while True:
    nimi=input("Syötä oppilaan nimi: ")
    if  nimi == "":
        break    
    oppilaita.append(nimi)
maara = len(oppilaita)
nimet = "," .join(oppilaita)
print(f"Oppilaiden määrä: {maara}")
print(nimet)