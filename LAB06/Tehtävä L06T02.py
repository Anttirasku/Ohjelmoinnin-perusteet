celsius = float(input("Syötä asteet Celsiuksena: "))
def cel_to_fah(celsius):
    to_fah = (celsius * 1.8) + 32
    return to_fah
farenheit = float(input("Syötä asteet Farenheit:ina: "))
def fah_to_cel(farenheit):
    to_cel = (farenheit - 32) / 1.8
    return to_cel
to_fah = cel_to_fah(celsius)
to_cel = fah_to_cel(farenheit)
print (f"{to_fah:.1f}, Farenheit-astetta")
print (f"{to_cel:.1f}, Celsius-astetta")