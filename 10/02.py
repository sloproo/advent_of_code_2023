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
        suunnat = ["U", "R", "D", "L"]
    
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

# Siistitään silmukkaan kuuluvat roskaputket pois

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


def menosuunta(lahto: tuple, kohde: tuple, putkisto: list = putkisto) -> str:
    if kohde[0] == lahto[0] + 1:
        return "D"
    elif kohde[0] == lahto[0] - 1:
        return "U"
    elif kohde[1] == lahto[1] + 1:
        return "R"
    elif kohde[1] == lahto[1] -1 :
        return "L"
    else:
        raise ValueError("Mitäs helvettiä")


kakkoskierros_kesken = True
while kakkoskierros_kesken:
    lahto = kakkoskierros[-1]
    if len(kakkoskierros) == 1:
        kohde = naapurit(lahto[0], lahto[1])[0]
    else:
        if naapurit(lahto[0], lahto[1])[0] not in kakkoskierros:
            kohde = naapurit(lahto[0], lahto[1])[0]
        elif naapurit(lahto[0], lahto[1])[1] not in kakkoskierros:
            kohde = naapurit(lahto[0], lahto[1])[1]
        else:
            print("Kakkoskierroksen matka valmis")
            kohde = alku
            kakkoskierros_kesken = False

    suunta = menosuunta(lahto, kohde)
    if suunta == "R":
        oikea = (kohde[0] + 1, kohde[1])
        vasen = (kohde[0] - 1, kohde[1])
    elif suunta == "D":
        oikea = (kohde[0], kohde[1] - 1)
        vasen = (kohde[0], kohde[1] + 1)
    elif suunta == "L":
        oikea = (kohde[0] - 1, kohde[1])
        vasen = (kohde[0] + 1, kohde[1])
    elif suunta == "U":
        oikea = (kohde[0], kohde[1] + 1)
        vasen = (kohde[0], kohde[1] - 1)
    else:
        raise ValueError("Mitäs helvettiä")
    
    
    if kelpo(oikea[0], oikea[1]) and oikea not in silmukka and oikea not in oikealla:
        oikealla.append(oikea)
        putkisto[oikea[0]][oikea[1]] = " "
    if kelpo(vasen[0], vasen[1]) and vasen not in silmukka and vasen not in vasemmalla:
        vasemmalla.append(vasen)
        putkisto[vasen[0]][vasen[1]] = "▀"
    kakkoskierros.append(kohde)

def ymparoivat(koordinaatti: tuple, putkisto: list = putkisto, silmukka: list = silmukka) -> list:
    y, x = koordinaatti
    kaikki = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
    palautettavat = [ehdokas for ehdokas in kaikki if kelpo(ehdokas[0], ehdokas[1])]
    return palautettavat

while True:
    oikea_kasvoi = False
    for oikeanpuoleinen in oikealla:
        for ymparoiva in ymparoivat(oikeanpuoleinen):
            if ymparoiva not in silmukka and ymparoiva not in oikealla:
                oikealla.append(ymparoiva)
                putkisto[ymparoiva[0]][ymparoiva[1]] = "▄"
                oikea_kasvoi = True
    if not oikea_kasvoi:
        break

while True:
    vasen_kasvoi = False
    for vasemmanpuoleinen in vasemmalla:
        for ymparoiva in ymparoivat(vasemmanpuoleinen):
            if ymparoiva not in silmukka and ymparoiva not in vasemmalla:
                vasemmalla.append(ymparoiva)
                putkisto[ymparoiva[0]][ymparoiva[1]] = " "
                vasen_kasvoi = True
    if not vasen_kasvoi:
        break

for koordinaatit in silmukka:
    y, x = koordinaatit
    putkisto[y][x] = "."

# print(f"Oikealla kasvatettu, {len(oikealla)}")
# print(oikealla)
# print(f"Vasemmalla kasvatettu, {len(vasemmalla)}")
# print(vasemmalla)
# pass

for koordinaatit in oikealla:
    if koordinaatit[0] == 0 or koordinaatit[1] == 0:
        print("Oikea ei käy")
        print(f"Haettu ruutujen määrä = {len(vasemmalla)}")
        break

for koordinaatit in vasemmalla:
    if koordinaatit[0] == 0 or koordinaatit[1] == 0:
        print("Vasen ei käy")
        print(f"Haettu ruutujen määrä = {len(oikealla)}")
        break

# pass

# for y in range(len(putkisto)):
#     for x in range(len(putkisto[y])):
#         if (y, x) not in silmukka and (y, x) not in oikealla and (y, x) not in vasemmalla:
#             print(f"Koordinaattia {y}, {x} ei ole missään")

# 346 348 liian pieni

# for koordinaatit in oikealla:
#     y, x = koordinaatit
#     putkisto[y][x] = "█"

# for koordinaatit in vasemmalla:
#     y, x = koordinaatit
#     putkisto[y][x] = " "

# for koordinaatit in silmukka:
#     putkisto[y][x] = "."

for y in range(len(putkisto)):
    for x in range(len(putkisto[y])):
        print(putkisto[y][x], end="")
    print()

pass

# for y in range(len(putkisto)):
#     for x in range(len(putkisto[y])):
#         if putkisto[y][x] not in [["█", " ", "."]]:
#             pass
