import datetime
from datetime import datetime
nimi=input("Anna nimesi:")
syntymavuosi=int(input("Kerro syntymävuotesi:"))
kuluvavuosi=datetime.now().year
ika=kuluvavuosi - syntymavuosi
print("Onnea ",nimi,"olet jo ",ika,"vanha!")