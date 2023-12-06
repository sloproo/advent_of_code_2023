siemenet = []
kartat = []
yhteensa = 0

with open("alku.txt") as f:
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
    ratkesi = False
    while not ratkesi:
        if nykytaso == -1:
            for haarukka in siemenhaarukat:
                if not ((alku < haarukka[0] and loppu < haarukka [0]) or \
                        (alku >= haarukka[0] + haarukka[1] and loppu >= haarukka[0] + haarukka[1])):
                    if alku >= haarukka[0]:
                        print(alku)
                        return (alku, True)
                    else:
                        return (haarukka[0], True)
                else:
                    print(loppu)
                    return (loppu, False)
        else:
            for alue in kartat[nykytaso]:
                if alue[0] > alku:
                    alku, ratkesi = ylos(alku, alue[0], nykytaso -1)
                elif alue[0] <= alku < alue[0] + alue[2]:
                    for hakukartta in kartat[nykytaso -1]:
                        if hakukartta[0] <= alku < hakukartta[0] + hakukartta[2]:
                            alku, ratkesi = ylos(hakukartta[1] + alku - alue[0], hakukartta[1] + hakukartta[2]-1, nykytaso-1)

print(ylos(0, 10**20, 6))
