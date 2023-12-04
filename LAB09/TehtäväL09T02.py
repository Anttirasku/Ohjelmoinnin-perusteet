#Jatkoa edelliseen. Tee ohjelma, joka lukee edellisessä tehtävässä luodusta tiedostosta nimet ja näyttää ne konsolilla. #
#Tämän jälkeen ohjelma lajittelee nimet aakkosjärjestykseen ja näyttää ne konsolilla aakkosjärjestyksessä.#
file = open("sukunimet.txt", "r")
lines = file.readlines()
print(lines)
file.close()