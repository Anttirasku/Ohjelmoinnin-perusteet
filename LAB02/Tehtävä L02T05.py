firstname=input("Syötä etunimesi  ")
first_letter=firstname[0:1]
lettercount=len(firstname)
print("Nimessäsi on",lettercount,"kirjainta.")
print(first_letter*lettercount)