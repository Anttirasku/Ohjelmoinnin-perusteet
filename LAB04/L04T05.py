fname = input("Anna etunimi: ")
surname = input("Anna sukunimi: ")
surname_backwards = surname[::-1]
firstletter = fname[0:1]
lettercount = len(fname)
print(firstletter*lettercount,surname_backwards)