class Human:
    name = ""
    age = 0
    def __str__(self):
        return "Nimi: " + self.name + " " "ikä: " + str(self.age)
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age
human1 = Human("Adam", 19)
human2 = Human("Eva", 18)
print(human1)
print(human2)