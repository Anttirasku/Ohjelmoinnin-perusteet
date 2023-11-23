class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def miau(self):
        return "Meoooooow!"
kissa1 = Cat("Kit", "black")
kissa2 = Cat("Kat", "white")
print(f"{kissa1.name}, color: {kissa1.color}")
print(f"{kissa2.name}, color: {kissa2.color}")
print(f"{kissa1.name} says: {kissa1.miau()}")
print(f"{kissa2.name} says: {kissa2.miau()}")