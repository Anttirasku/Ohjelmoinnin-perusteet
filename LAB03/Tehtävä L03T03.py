inserted_number=int(input("Syötä numero: "))
list1=[10,20]
list2=[100,200]
if inserted_number in list1:
    print("Kokonaislukusi on 10 tai 20")
elif inserted_number in list2:
    print("Kokonaislukusi on 100 tai 200")
elif inserted_number not in list1:
    print("Luku on ",inserted_number)
elif inserted_number not in list2:
    print("Luku on ",inserted_number)