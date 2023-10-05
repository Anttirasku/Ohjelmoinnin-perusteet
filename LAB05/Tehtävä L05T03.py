def average(arvo1, arvo2, arvo3,):
    return (arvo1 + arvo2 + arvo3)/syottojen_maara
try:
    arvo1 = float(input("Anna ensimmäinen parametri: "))
    arvo2 = float(input("Anna toinen parametri: "))
    arvo3 = float(input("Anna kolmas parametri: "))
    syottojen_maara = 3 
    keskiarvo = average(arvo1, arvo2, arvo3)
    print(f"{keskiarvo:.1f}")
except ValueError:
    print("Virheellinen syöttö")