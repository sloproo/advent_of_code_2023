import re

rivit = []

with open("alku.txt") as f:
    for r in f:
        jouset, luvut = r.strip().split(" ")
        jouset = "." + (jouset + "?") * 5 + "."
        luvut = [int(luku) for luku in luvut.split(",")] * 5
        rivit.append((jouset, luvut))

def kelvollinen(rivi: tuple) -> int:
    jouset, luvut = rivi
    alun_jouset = jouset
    for i in range(len(luvut)):
        indeksi = jouset.find("#")
        if indeksi == -1:
            return 0
        if jouset[indeksi:indeksi+luvut[i]+1] != "#" * luvut[i] + ".":
            return 0
        jouset = jouset[indeksi+luvut[i]+1:]
    if "#" in jouset:
        return 0
    return 1

def mahdollisia_rivista(rivi: tuple) -> int:
    mahdollisia = 0
    jouset, luvut = rivi

    for luku in luvut:
        hakulauseke = re.search(f"(?=([\.\?][#\?]{{{luku}}}[\.\?]))", jouset)
        pass


    if "?" in jouset:
        jokeri = jouset.find("?")
        mahdollisia += mahdollisia_rivista((jouset[:jokeri] + "#" + jouset[jokeri+1:], luvut))
        mahdollisia += mahdollisia_rivista((jouset[:jokeri] + "." + jouset[jokeri+1:], luvut))
    else:
        mahdollisia += kelvollinen(rivi)
    return mahdollisia

mahdollisia_kaikkiaan = 0

ratkottu = 0
for rivi in rivit:
    mahdollisia_kaikkiaan += mahdollisia_rivista(rivi)
    ratkottu += 0
    print(f"Rivi {ratkottu} ratkaistu ")
    
print(mahdollisia_kaikkiaan)


