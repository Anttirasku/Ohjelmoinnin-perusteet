def get_fuel(ajettu_matka, keskikulutus):
    kulutus = (ajettu_matka / 100) * keskikulutus
    return kulutus
ajettu_matka = int(input("Anna kilometrimäärä: "))
keskikulutus = float(input("Anna keskikulutuksesi, käytä pistettä desimaalierottimena: "))
kulutus = get_fuel(ajettu_matka, keskikulutus)
print(f"{kulutus:.1f} ltr")