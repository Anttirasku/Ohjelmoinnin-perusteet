arvosanat = []
while True:
    try:   
        arvosana = int(input("Syötä kurssin arvosana väliltä 0-5: "))
        if arvosana >= 0 and arvosana <=5:
            arvosanat.append(arvosana)
        else:
            print("Sinun pitää antaa kurssin arvosana väliltä 0-5: ")
    except ValueError:
            break
keskiarvo = sum(arvosanat) / len(arvosanat)
print("Arvosanoja annettu: ",len(arvosanat))
print("Arvosanojen keskiarvo oli: ", (keskiarvo))