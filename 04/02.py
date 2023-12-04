kortit = []

with open("input.txt") as f:
    for r in f:
        r = r.strip().split(":")[1]
        r = r.replace("  ", " ")
        voitot, annetut = (puoli.strip() for puoli in r.split("|"))
        kortit.append((1, [int(voitto) for voitto in voitot.split(" ")], [int(annettu) for annettu in annetut.split(" ")]))

voitot = 0

for i in range(len(kortit)):
    osumia = 0
    for annettu in kortit[i][2]:
        if annettu in kortit[i][1]:
            osumia += 1
    for j in range(i+1, i+1+osumia):
        if j < len(kortit):
            kortit[j] = (kortit[j][0] + kortit[i][0] * 1, kortit[j][1], kortit[j][2])

print(sum(kortti[0] for kortti in kortit))
