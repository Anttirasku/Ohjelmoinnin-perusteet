def get_cost(ajettu_matka, keskikulutus, ltr_hinta):
    ajomatkan_hinta = ((ajettu_matka / 100)*keskikulutus)*ltr_hinta
    return ajomatkan_hinta

ajettu_matka = int(input("Anna ajokilometrisi: "))
keskikulutus = float(input("Ilmoita keskikulutuksesi, käytä desimaali erottimena pistettä: "))
ltr_hinta = float(input("Syötä litrahinta, käytä desimaali erottimena pistettä: "))
ajomatkan_hinta = get_cost(ajettu_matka, keskikulutus, ltr_hinta)
print(f"Matkan hinta on: {ajomatkan_hinta:.2f}")