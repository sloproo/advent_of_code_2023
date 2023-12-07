import string

def tulos(kortit: list) -> int:
    lukumaarat = [kortit.count(kortti) for kortti in kortit]
    if max(lukumaarat) == 5:
        return 1
    if max(lukumaarat) == 4:
        return 2
    if max(lukumaarat) == 3:
        if min(lukumaarat) == 2:
            return 3
        else:
            return 4
    if lukumaarat.count(2) == 4:
        return 5
    if lukumaarat.count(2) == 2:
        return 6
    if max(lukumaarat) == 1:
        return 7

kadet = []

with open ("alku.txt") as f:
    for r in f:
        r = r.strip().split(" ")
        kortit = []
        for kortti in r[0]:
            if kortti in string.digits:
                kortit.append(int(kortti))
            elif kortti == "A":
                kortit.append(14)
            elif kortti == "K":
                kortit.append(13)
            elif kortti == "Q":
                kortit.append(12)
            elif kortti == "J":
                kortit.append(11)
            elif kortti == "T":
                kortit.append(10)
            else:
                print("Nyt tuli omituinen kortti")
                raise ValueError("mitäs")
        kadet.append((kortit, tulos(kortit), int(r[1])))

lajiteltu = sorted(kadet, key=lambda k: (-k[1], k[0][0], k[0][1], k[0][2], k[0][3], k[0][4]))

for i in range(len(lajiteltu)):
    lajiteltu[i] = lajiteltu[i] + (i+1, lajiteltu[i][2] * (i+1))

print(sum([kasi[4] for kasi in lajiteltu]))