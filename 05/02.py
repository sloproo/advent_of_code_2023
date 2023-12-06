siemenet = []
kartat = []
yhteensa = 0

with open("input.txt") as f:
    siemennumerot = [int(siemennro) for siemennro in f.readline().split(":")[1].strip().split(" ")]
    siemenhaarukat = [(siemennumerot[i], siemennumerot[i+1]) for i in range(0, len(siemennumerot), 2)]
    f.readline()
    f.readline()
    kartta = []
    for r in f:
        if r =="\n":
            kartat.append(kartta)
            kartta = []
            f.readline()
        else:
            kohde, lahde, pituus = (r.strip().split(" "))
            kartta.append((int(kohde), int(lahde), int(pituus)))
    kartat.append(kartta)

siemenhaarukat = sorted(siemenhaarukat, key= lambda haarukka: haarukka[0])
for i in range(len(kartat)):
    kartat[i] = sorted(kartat[i], key= lambda saannot: saannot[0])

def ylos(alku: int, loppu: int, nykytaso: int, kartat: list = kartat) -> tuple:
    if nykytaso == -1:
        for haarukka in siemenhaarukat:
            if haarukka[0] <= alku < haarukka[0] + haarukka[1] or 
            haarukka[0] <= loppu < haarukka[0] + haarukka[1]



kokeiltava = 0
while not loytyi:
    lahtopaikka
    for i in range(len(kartat) -1, -1, -1):
        for j in range(len(kartat[i])):
            if kokeiltava < kartat[i][j][0]:
                break
            elif kokeiltava < kartat[i][j][0] + kartat[i][j][2]:
                kokeiltava += kartat[i][j][1] - kartat[i][j][0]
                break
    for haarukka in siemenhaarukat:
        if haarukka[0] <= kokeiltava < haarukka[0] + haarukka[1]:
            loytyi = True

lahtopaikka -= 1
print(lahtopaikka)
