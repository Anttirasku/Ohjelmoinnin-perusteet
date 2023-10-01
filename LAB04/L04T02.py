summa = 0
for i in range(7):
    a = int(input("Sademäärä: "))
    if a>0:
        summa = summa+a
print(f"Viikon sademäärä yhteensä: {summa}")