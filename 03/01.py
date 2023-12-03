import string

def naapurit(luku: tuple, piirros: list) -> list:
    palautus = []
    pysty, alku, loppu = luku[1], luku[2], luku[3]

    if pysty > 0:
        if alku > 0:
            palautus.append((pysty-1, alku-1))
        palautus += [(pysty-1, x) for x in range(alku, loppu + 1)]
        if loppu +1 < len(piirros[pysty]):
            palautus.append((pysty-1, loppu+1))
    if alku > 0:
        palautus.append((pysty, alku-1))
    if loppu + 1 < len(piirros[pysty]):
        palautus.append((pysty, loppu+1))
    if pysty + 1 < len(piirros):
        if alku > 0:
            palautus.append((pysty+1, alku-1))
        palautus += [(pysty+1, x) for x in range(alku, loppu + 1)]
        if loppu +1 < len(piirros[pysty]):
            palautus.append((pysty+1, loppu+1))
    # if pysty == len(piirros) -1:
    #     print(f"luvun {luku[0]} koordinaateissa y = {luku[1]}, x = {luku[2]} - {luku[3]} naapureita ovat")
    #     print(palautus)
    #     pass
    return palautus

piirros = []
luvut = []

with open("input.txt") as f:
    for r in f:
        piirros.append([merkki for merkki in r.strip()])

lukusana = ""
for y in range(len(piirros)):
    for x in range(len(piirros[y])):
        if piirros[y][x] in string.digits:
            if lukusana == "":
                alku = x
            lukusana += piirros[y][x]
            if x == len(piirros[y]) - 1:
                loppu = x
                luvut.append((int(lukusana), y, alku, loppu))
                lukusana = ""        
        elif lukusana != "":
            loppu = x-1
            luvut.append((int(lukusana), y, alku, loppu))
            lukusana = ""

summattavat = 0
hylatyt = 0

for luku in luvut:
    kaytetty = False
    for naapuri in naapurit(luku, piirros):
        if kaytetty:
            break
        if piirros[naapuri[0]][naapuri[1]] != "." and piirros[naapuri[0]][naapuri[1]] not in string.digits:
            summattavat += luku[0]
            kaytetty = True
            print(f"lisätään luku {luku[0]} koordinaateissa y = {luku[1]}, x = {luku[2]} - {luku[3]} summattaviin")
            print(f"Koska sen naapuri {naapuri[0]}, {naapuri[1]} on symboli {piirros[naapuri[0]][naapuri[1]]}\n")
            pass
            break
    else:
        print(f"hylätään luku {luku[0]} koordinaateissa y = {luku[1]}, x = {luku[2]} - {luku[3]} summattaviin\n")
        hylatyt += luku[0]
        pass

print(summattavat)
print(hylatyt)

print(sum([luku[0] for luku in luvut]))

# print(hylatyt)

# 1763175 liian iso
# 1761233 liian iso
# 1759938 liian iso
# 554003 oikein
