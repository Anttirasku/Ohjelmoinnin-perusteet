pisteet = []
for i in range(5):
    piste =int(input("Arvosana"))
    pisteet.append(piste)
pisteet.sort()
pisteet=pisteet[1:-1]
summa = 0
for piste in pisteet:
    summa=summa+piste
print(summa)