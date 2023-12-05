kartat = []

with open("input.txt") as f:
    siemenet = [[int(siemennro)] for siemennro in f.readline().split(":")[1].strip().split(" ")]
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
    
for i in range(len(kartat)):
    for siemen in siemenet:
        for saanto in kartat[i]:
            if siemen[i] in range(saanto[1], saanto[1] + saanto[2] + 1):
                siemen.append(saanto[0] + siemen[i] - saanto[1])
                break
        else:
            siemen.append(siemen[i])
    

print(min([siemen[7] for siemen in siemenet]))
