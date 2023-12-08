import re, math

with open ("input.txt") as f:
    haarat = {}
    suunnat = f.readline().strip()
    f.readline()
    for r in f:
        paikat = re.findall("[0-9A-Z]{3}", r)
        haarat[paikat[0]] = (paikat[1], paikat[2])

askeleita = 0
maalissa = False
kummitusten_paikat = [alku for alku in haarat.keys() if alku[-1] == "A"]
kummitusten_maalivuorot = {}
for i in range(len(kummitusten_paikat)):
    kummitusten_maalivuorot[i] = []

while not maalissa:
    for suunta in suunnat:
        askeleita += 1
        for i in range(len(kummitusten_paikat)):
            if suunta == "L":
                kummitusten_paikat[i] = haarat[kummitusten_paikat[i]][0]
            elif suunta == "R":
                kummitusten_paikat[i] = haarat[kummitusten_paikat[i]][1]
            if kummitusten_paikat[i][-1] =="Z":
                kummitusten_maalivuorot[i].append(askeleita)
        if min(([len(maalivuorot) for maalivuorot in kummitusten_maalivuorot.values()])) == 5:
            for i in range(len(kummitusten_maalivuorot)):
                if kummitusten_maalivuorot[i][-1] - kummitusten_maalivuorot[i][-2] == \
                kummitusten_maalivuorot[i][-2] - kummitusten_maalivuorot[i][-3] == \
                kummitusten_maalivuorot[i][-3] - kummitusten_maalivuorot[i][-4] == \
                kummitusten_maalivuorot[i][-4] - kummitusten_maalivuorot[i][-5]:
                    pass
                else:
                    break
            else:
                kummitusten_syklit = [kummitusten_maalivuorot[i][-1] - kummitusten_maalivuorot[i][-2] for i in range(len(kummitusten_paikat))]
                maalissa = True

print(math.lcm(*kummitusten_syklit))
