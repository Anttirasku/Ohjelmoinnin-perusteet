##  Lataa tämä tekstitiedosto nimet.txt koneellesi. Tiedostossa on henkilöitten nimiä.  ##
##  Sama nimi saattaa esiintyä monta kertaa.                                            ##
##  Tee ohjelma, joka lukee em. tekstitiedostosta nimet ja kertoo montako nimeä löytyy- ##
##  ja montako kertaa kukin nimi esiintyy. Käytä Dictionary-kokoelmaa ratkaisussasi.    ##
filename = "nimet.txt"
name_counts = {}
with open(filename, "r") as file:
    for line in file:
        name = line.strip()
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
print("Nimiä yhteensä:", len(name_counts))
print("\nNimien esiintymiskerrat:")
for name, count in name_counts.items():
    print(f"{name}: {count} kertaa")
