class Vehicle:
    brand = ""
    model = ""
    power_hp = 0
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.power_hp) + "hp"
    def __init__(self, brand = "", model = "", power = 0):
        self.brand = brand
        self.model = model
        self.power_hp = power
sportcar = Vehicle("Volvo","240", 106)
print(sportcar)