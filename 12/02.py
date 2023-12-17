import re

rivit = []

with open("alkuh.txt") as f:
    for r in f:
        jouset, luvut = r.strip().split(" ")

        # erikseen lopulliset ja simppelit testauskäyttöön
        # jouset = "." + (jouset + "?") * 5 + "."
        # luvut = [int(luku) for luku in luvut.split(",")] * 5

        jouset = "." + jouset + "."
        luvut = [int(luku) for luku in luvut.split(",")]

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
        eka_varma = re.search(f"[\.\?][#]{{{luku}}}[\.\?]", jouset)

        eka_mahdollinen = re.search(f"[\.\?][#\?]{{{luku}}}[\.\?]", jouset)
        mahdolliset = list(re.finditer(f"(?=([\.\?][#\?]{{{luku}}}[\.\?]))", jouset))

        if len(mahdolliset) == 0:
            return 0
        if len(luvut) == 1:
            for mahdollinen in mahdolliset:
                mahdollisia += kelvollinen(("." + jouset[mahdollinen.start() + luvut[0] + 2:], luvut))
            return mahdollisia

        print(f"eka varma: {eka_varma}")
        print(f"eka varma: {eka_mahdollinen}")

        
        
        if eka_varma != None:
            varman_alku = eka_varma.start()
            mahdollisen_alku = eka_mahdollinen.start()
            if varman_alku <= eka_mahdollinen.start():
                print("Oha se varma")
                mahdollisia += mahdollisia_rivista(("." + jouset[varman_alku + luku + 2:], luvut[1:]))
        elif eka_mahdollinen != None:
            mahdollisen_alku = eka_mahdollinen.start()
            print("kokeillaan mahdollisuutta")
            mahdollisia += mahdollisia_rivista(("." + jouset[mahdollisen_alku + luku + 2:], luvut[1:]))
        return mahdollisia    


mahdollisia_kaikkiaan = 0

ratkottu = 0
for rivi in rivit:
    mahdollisia_kaikkiaan += mahdollisia_rivista(rivi)
    ratkottu += 1
    print(f"Rivi {ratkottu} ratkaistu ")
    
print(mahdollisia_kaikkiaan)


