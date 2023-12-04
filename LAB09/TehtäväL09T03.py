##   Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja ja tallentaa annetut luvut tiedostoon luvut.txt.     ##
##   Ohjelma lopettaa lukujen kysymisen, kun käyttäjä antaa tyhjän syötteen.                                 ##
##   Viimeiseksi ohjelma kirjoittaa tiedostoon montako lukua käyttäjä antoi                                  ##
##   seuraavasti: Syötetty 5 lukua. Tarkista lopuksi tiedoston sisältö tekstieditorilla.                     ##
filename = "luvut.txt"
file = open(filename, "a")
i = 0
while True:
        number = input("Syötä kokonaisluku, tyhjä syöte lopettaa ohjelman: ")
        if not number:
            break
        number = int(number)
        file.write(str(number) + "\n")
        i += 1
print("Syötetty ", i, " lukua.")