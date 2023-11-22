pisteet = []
for i in range(5):
    while True:
        piste =int(input("Hypyn pisteet: "))
        if piste>0 and piste <=20:
            break
        
    pisteet.append(piste)
pisteet.sort()
pisteet=pisteet[1:-1]
summa = 0
for piste in pisteet:
    summa=summa+piste
print("Pisteet yheensä: ",summa)