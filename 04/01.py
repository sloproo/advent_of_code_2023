kortit = []

with open("input.txt") as f:
    for r in f:
        r = r.strip().split(":")[1]
        r = r.replace("  ", " ")
        voitot, annetut = (puoli.strip() for puoli in r.split("|"))
        kortit.append(([int(voitto) for voitto in voitot.split(" ")], [int(annettu) for annettu in annetut.split(" ")]))

voitot = 0

for kortti in kortit:
    osumia = 0
    for annettu in kortti[1]:
        if annettu in kortti[0]:
            osumia += 1
    if osumia > 0:
        voitot += 2**(osumia-1)

print(voitot)
