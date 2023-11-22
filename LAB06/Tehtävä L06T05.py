def show_cm(tuuma): 
    sentit = (tuuma / 0.3937)
    return sentit
tuuma = float(input("Syötä tuumat: "))
sentit = show_cm(tuuma)
print(tuuma,"tuumaa on ",f"{sentit:.2f}","cm")