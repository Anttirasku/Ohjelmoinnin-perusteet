def subtract(arvo1, arvo2):
    return arvo1 - arvo2
try:
    arvo1 = int(input("Anna ensimmäinen parametri: "))
    arvo2 = int(input("Anna toinen parametri: "))
    laskutulos = subtract(arvo1, arvo2)
    print(laskutulos)
except ValueError:
    print("Virheellinen syöttö")