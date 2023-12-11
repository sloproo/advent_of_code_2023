import itertools

avaruus = []
tyhjat_rivit = []
tyhjat_palkit = []

def matka(eka: tuple, toka: tuple, tyhjat_palkit: list = tyhjat_palkit, tyhjat_rivit: list = tyhjat_rivit) -> int:
    palautettava = abs(eka[0] - toka[0]) + abs(eka[1] - toka[1])
    ylitettavat_tyhjat_rivit = 0
    ylitettavat_tyhjat_palkit = 0
    for y in range(min(eka[0]+1, toka[0]), max(eka[0], toka[0])):
        if y in tyhjat_rivit:
            ylitettavat_tyhjat_rivit += 1
    for x in range(min(eka[1]+1, toka[1]), max([eka[1], toka[1]])):
        if x in tyhjat_palkit:
            ylitettavat_tyhjat_palkit += 1

    kasvukerroin = 1000000
    palautettava += (kasvukerroin - 1) * (ylitettavat_tyhjat_rivit + ylitettavat_tyhjat_palkit)
    return palautettava

with open("input.txt") as f:
    for r in f:
        avaruus.append([merkki for merkki in r.strip()])

galaksit = []

for y in range(len(avaruus)):
    if len(set([avaruus[y][x] for x in range(len(avaruus[y]))])) == 1:
        tyhjat_rivit.append(y)
    elif len(set([avaruus[y][x] for x in range(len(avaruus[y]))])) != 2:
        raise ValueError("Mitäs helvettiä")
    for x in range(len(avaruus[y])):
        if avaruus[y][x] == "#":
            galaksit.append((y, x))
    

for x in range(len(avaruus[0])):
    if len(set([avaruus[y][x] for y in range(len(avaruus))])) == 1:
        tyhjat_palkit.append(x)
    elif len(set([avaruus[y][x] for y in range(len(avaruus))])) != 2:
        raise ValueError("Mitäs helvettiä")
  
galaksiparit = [pari for pari in itertools.combinations(galaksit, 2)]

matkaa_yhteensa = 0
for pari in galaksiparit:
    matkaa_yhteensa += matka(pari[0], pari[1])

print(matkaa_yhteensa)