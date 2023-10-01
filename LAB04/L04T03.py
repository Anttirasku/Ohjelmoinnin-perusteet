syotteiden_maara=0
syotteiden_summa=0
while True:
    syote=input("Syötä lukusi!")
    if syote=="":
        break
    syotteiden_summa+=int(syote)
    syotteiden_maara+=1
print("Lukuja annettu: ",syotteiden_maara)
print("Lukujen summa: ",syotteiden_summa)