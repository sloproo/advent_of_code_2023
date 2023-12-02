pelit = []

with open("input.txt") as f:
    for r in f:
        pelin_nro = int(r.split(" ")[1][:-1])
        peli = r.split(":")[1]
        naytot = []
        for naytto in peli.strip().split(";"):
            nayton_nopat = []
            nopat = naytto.strip().split(", ")
            for noppa in nopat:
                noppa = noppa.strip().split(" ")
                maara = int(noppa[0])
                vari = noppa[1]
                nayton_nopat.append((maara, vari))
            naytot.append(nayton_nopat)
        pelit.append((pelin_nro, naytot))
    
    pelinrojen_summa = 0
    for peli in pelit:
        pielessa = False
        for naytto in peli[1]:
            for noppa in naytto:
                if (noppa[0] > 12 and noppa[1] == "red") or \
                (noppa[0] > 13 and noppa[1] == "green") or \
                (noppa[0] > 14 and noppa[1] == "blue"):
                    pielessa = True
                    break
            if pielessa:
                break
        if not pielessa:
            pelinrojen_summa += peli[0]

print(pelinrojen_summa)
