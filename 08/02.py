import re

with open ("input.txt") as f:
    haarat = {}
    suunnat = f.readline().strip()
    f.readline()
    for r in f:
        paikat = re.findall("[A-Z]{3}", r)
        haarat[paikat[0]] = (paikat[1], paikat[2])

print(suunnat)
print(haarat)
pass

askeleita = 0
maalissa = False
oma_paikka = "AAA"

while not maalissa:
    for suunta in suunnat:
        print(oma_paikka)
        askeleita += 1
        if suunta == "L":
            oma_paikka = haarat[oma_paikka][0]
            print(f"Suunta on {suunta}, mennään paikkaan {oma_paikka}")
        elif suunta == "R":
            oma_paikka = haarat[oma_paikka][1]

        if oma_paikka == "ZZZ":
            maalissa = True
            break

print(askeleita)
