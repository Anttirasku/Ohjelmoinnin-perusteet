while True:
    try:
        luku = int(input("Syötä luku väliltä 1-10: "))
        if 1 <= luku <= 10:
            break
        else:
            print("Syötä numero väliltä 1-10: ")
    except ValueError:
        print("Syötä kokonaisluku!")
for i in range(1, luku + 1):
    print(f"Luvun {i} neliö on {i*i}")