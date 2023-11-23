class Vehicle:
    brand = ""
    model = ""
    power_kw = 0
mycar = Vehicle()

mycar.brand = input("Kerro mikä automerkki: ")
mycar.model = input("Kerro mikä automalli: ")
mycar.power_kw = input("Paljonko siinä on tehoa: ")

print("Minulla on ",mycar.brand,mycar.model," siinä on ", mycar.power_kw," kilowattia voimaa!")