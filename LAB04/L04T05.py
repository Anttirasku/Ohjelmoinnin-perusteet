fname = input("Anna etunimi: ")
surname = input("Anna sukunimi: ")
for _ in range(len(fname)):
    print(fname[0], end="")
surname_backwards = surname[::-1]
print(" ",surname_backwards)