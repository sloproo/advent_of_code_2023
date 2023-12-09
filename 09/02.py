rivit = []

with open("input.txt") as f:
    for r in f:
        rivin_luvut = [int(luku) for luku in r.split()]
        rivit.append(rivin_luvut)

def kasvut(luvut: list) -> list:
    palautettava = []
    for i in range(1, len(luvut)):
        palautettava.append(luvut[i] - luvut[i-1])
    return palautettava

ratkotut_rivit = []
for rivi in rivit:
    ratkottavat_rivit = [rivi]
    while set(rivi) != {0}:
        rivi = kasvut(rivi)
        ratkottavat_rivit.append(rivi)
    # print(ratkottavat_rivit)
    for i in range(len(ratkottavat_rivit)-2, -1, -1):
        ratkottavat_rivit[i].insert(0, ratkottavat_rivit[i][0] - ratkottavat_rivit[i+1][0])
    ratkotut_rivit.append(ratkottavat_rivit[0])

print(sum([ratkottu[0] for ratkottu in ratkotut_rivit]))
