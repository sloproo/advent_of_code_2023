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
    for i in range(len(ratkottavat_rivit)-2, -1, -1):
        ratkottavat_rivit[i].append(ratkottavat_rivit[i][-1] + ratkottavat_rivit[i+1][-1])
    ratkotut_rivit.append(ratkottavat_rivit[0])
    
print(sum([ratkottu[-1] for ratkottu in ratkotut_rivit]))
