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
    
tulojen_summa = 0
for peli in pelit:
    pienimmat = {"red": 0, "green": 0, "blue": 0}
    for naytto in peli[1]:
        for noppa in naytto:
            if noppa[0] > pienimmat[noppa[1]]:
                pienimmat[noppa[1]] = noppa[0]
    tulojen_summa += pienimmat["red"] * pienimmat["blue"] * pienimmat["green"]

print(tulojen_summa)

