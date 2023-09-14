kokonimi=input("Syötä nimesi")
valilyonti=kokonimi.find(" ")
etunimi=kokonimi[:valilyonti]
sukunimi=kokonimi[valilyonti+1:]
print("Etunimesi on: ",etunimi,"ja sukunimesi on: ",sukunimi)