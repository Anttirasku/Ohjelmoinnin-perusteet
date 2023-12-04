#   Tee ohjelma, joka kysyy käyttäjältä henkilöiden sukunimiä ja kirjoittaa käyttäjän antamat nimet tiedostoon. #
#   Nimiä kysytään niin kauan kunnes käyttäjä antaa tyhjän syötteen. Huomioi mahdolliset poikkeukset, joita tiedoston käsittely voi aiheuttaa. #
filename = "sukunimet.txt"
file = open(filename, "w")
surname = "*"
i = 0
while surname != "":
    surname = input("Syötä sukunimi, tyhjä syöte lopettaa ohjelman: ")
    if surname != "":
        file.write(surname + "\n")
        i += 1
file.close()