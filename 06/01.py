import math

with open("input.txt") as f:
    ajat = [int(aika) for aika in f.readline().split(":")[1].split()]
    matkat = [int(matka) for matka in f.readline().split(":")[1].split()]

voitot = []
for kisa in range(len(matkat)):
    voittoja = 0
    for painoaika in range(ajat[kisa]):
        if painoaika * (ajat[kisa] - painoaika) > matkat[kisa]:
            voittoja += 1
        elif voittoja > 0:
            break
    voitot.append(voittoja)

print(math.prod(voitot))
