putkisto = []
with open("input.txt") as f:
    for r in f:
        putkisto.append([c for c in r.strip()])

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
        if 0 <= koordinaatit[0] < len(putkisto) and 0 <= koordinaatit[1] < len(putkisto[koordinaatit[0]]):
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

kaydyt = [alku] + naapurit(alku[0], alku[1])
matkat = {0: [alku], 1: naapurit(alku[0], alku[1])}
pass
for i in range(2, len(putkisto) * len(putkisto[0]) - 1):
    seuraavat = []
    for naapuri in matkat[i - 1]:
        kokeiltavat = naapurit(naapuri[0], naapuri[1])
        for kokeiltava in kokeiltavat:
            if kokeiltava not in kaydyt:    
                seuraavat.append(kokeiltava)
                kaydyt.append(kokeiltava)
    if len(seuraavat) == 0:
        break
    else:
        matkat[i] = seuraavat

# Vähän ufoo, myönnän
print(len(matkat) - 1)

