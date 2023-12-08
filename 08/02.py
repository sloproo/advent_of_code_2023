import re

with open ("input.txt") as f:
    haarat = {}
    suunnat = f.readline().strip()
    f.readline()
    for r in f:
        paikat = re.findall("[0-9A-Z]{3}", r)
        print(paikat)
        haarat[paikat[0]] = (paikat[1], paikat[2])

askeleita = 0
maalissa = False
kummitusten_paikat = [alku for alku in haarat.keys() if alku[-1] == "A"]

while not maalissa:
    for suunta in suunnat:
        askeleita += 1
        for i in range(len(kummitusten_paikat)):
            if suunta == "L":
                kummitusten_paikat[i] = haarat[kummitusten_paikat[i]][0]
                # print(f"Suunta on {suunta}, mennään paikkaan {kummitusten_paikat[i]}")
            elif suunta == "R":
                kummitusten_paikat[i] = haarat[kummitusten_paikat[i]][1]
        
        for kummitus in kummitusten_paikat:
            if kummitus[-1] != "Z":
                break
        else:
            maalissa = True
            break
        
print(askeleita)
