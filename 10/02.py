putkisto = []
with open("input.txt") as f:
    for r in f:
        putkisto.append([c for c in r.strip()])

def kelpo(y: int, x: int, putkisto: list = putkisto) -> bool:
    if 0 <= y < len(putkisto) and 0 <= x < len(putkisto[y]):
        return True
    return False

def naapurit(y: int, x: int, takaisin: bool = False, putkisto: list = putkisto) -> list:
    mahdolliset = []
    avoimet = []
    palautettavat = []
    if putkisto[y][x] == ".":
        return []
    elif putkisto[y][x] == "|":
        suunnat = ["U", "D"]
    elif putkisto[y][x] == "-":
        suunnat = ["L", "R"]
    elif putkisto[y][x] == "L":
        suunnat = ["U", "R"]
    elif putkisto[y][x] == "J":
        suunnat = ["U", "L"]
    elif putkisto[y][x] == "7":
        suunnat = ["L", "D"]
    elif putkisto[y][x] == "F":
        suunnat = ["D", "R"]
    elif putkisto[y][x] == "S":
        suunnat = ["U", "R", "D", "l"]
    
    if "U" in suunnat:
        mahdolliset.append((y - 1, x))
    if "R" in suunnat:
        mahdolliset.append((y, x + 1))
    if "D" in suunnat:
        mahdolliset.append((y + 1, x))
    if "L" in suunnat:
        mahdolliset.append((y, x - 1))
    for koordinaatit in mahdolliset:
        if kelpo(koordinaatit[0], koordinaatit[1]):
            avoimet.append(koordinaatit)
    if not takaisin:
        for koordinaatit in avoimet:
            if (y, x) in naapurit(koordinaatit[0], koordinaatit[1], True):
                palautettavat.append(koordinaatit)
        return palautettavat
    else:
        return avoimet
    
def aloituspaikka(putkisto: list = putkisto) -> tuple:
    for y in range(len(putkisto)):
        for x in range(len(putkisto[y])):
            if putkisto[y][x] == "S":
                return (y, x)
            
alku = aloituspaikka()

# Silmukan muodostus

silmukka = [alku] + naapurit(alku[0], alku[1])
matkat = {0: [alku], 1: naapurit(alku[0], alku[1])}

for i in range(2, len(putkisto) * len(putkisto[0]) - 1):
    seuraavat = []
    for naapuri in matkat[i - 1]:
        kokeiltavat = naapurit(naapuri[0], naapuri[1])
        for kokeiltava in kokeiltavat:
            if kokeiltava not in silmukka:    
                seuraavat.append(kokeiltava)
                silmukka.append(kokeiltava)
    if len(seuraavat) == 0:
        break
    else:
        matkat[i] = seuraavat

# Aloitusruutu oikean muotoiseksi

alun_naapurit = naapurit(alku[0], alku[1])
y, x = alku
if (y+1, x) in alun_naapurit and (y-1, x) in alun_naapurit:
    putkisto[y][x] = "|"
elif (y, x-1) in alun_naapurit and (y, x+0) in alun_naapurit:
    putkisto[y][x] = "-"
elif (y-1, x) in alun_naapurit and (y, x+1) in alun_naapurit:        
    putkisto[y][x] = "L"
elif (y+1, x) in alun_naapurit and (y, x+1) in alun_naapurit:
    putkisto[y][x] = "F"
elif (y-1, x) in alun_naapurit and (y, x-1) in alun_naapurit:
    putkisto[y][x] = "J"
elif (y+1, x) in alun_naapurit and (y, x-1) in alun_naapurit:
    putkisto[y][x] = "7"
else:
    raise ValueError("Mitäs helvettiä nyt")


ulkopuoliset = []


for y in range(len(putkisto)):
    for x in range(len(putkisto[y])):
        if (y, x) not in silmukka:
            ulkopuoliset.append((y, x))
            putkisto[y][x] = "."

for y in range(len(putkisto)):
    for x in range(len(putkisto[y])):
        print(putkisto[y][x], end="")
    print()

kakkoskierros = [alku]
oikealla = []
vasemmalla = []

while True:
    
    if len(kakkoskierros) == 1:
        kakkoskierros.append(naapurit(kakkoskierros[0][0], kakkoskierros[0][1])[0])
    else:
        if naapurit(kakkoskierros[-1][0], kakkoskierros[-1][1])[0] not in kakkoskierros:
            kakkoskierros.append(naapurit(kakkoskierros[-1][0], kakkoskierros[-1][1])[0])
        elif naapurit(kakkoskierros[-1][0], kakkoskierros[-1][1])[1] not in kakkoskierros:
            kakkoskierros.append(naapurit(kakkoskierros[-1][0], kakkoskierros[-1][1])[1])
        else:
            print("Kakkoskierroksen matka valmis")
            kakkoskierros.append(alku)
            break

for i in range(1, len(kakkoskierros)):
    lahto = kakkoskierros[i - 1]
    maali = kakkoskierros[i]
    if maali[0] - lahto[0] == -1:
        suunta = "D"
    elif maali[0] - lahto[0] == 1:
        suunta = "U"
    elif maali[1] - lahto[1] == -1:
        suunta = "L"
    elif maali[1] - lahto[1] == 1:
        suunta = "R"
    else:
        raise ValueError("Mitäs helvettiä")
    