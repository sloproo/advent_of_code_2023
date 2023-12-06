with open("input.txt") as f:
    aika = int("".join([luku for luku in f.readline().split(":")[1].split()]))
    matka = int("".join([luku for luku in f.readline().split(":")[1].split()]))

def voitto(painoaika: int, aika: int = aika, matka: int = matka) -> bool:
    return painoaika * (aika - painoaika) > matka

pienin_voitto, suurin_voitto = aika, 0
pienin_ratkaistu, suurin_ratkaistu = False, False
haun_jakaja = 2

while pienin_voitto == aika:
    for i in range(1, haun_jakaja, 2):
        hakuaika = i * (aika // haun_jakaja)
        if voitto(hakuaika):
            if hakuaika < pienin_voitto:
                pienin_voitto = hakuaika
            if hakuaika > suurin_voitto:
                suurin_voitto = hakuaika
            
    haun_jakaja *= 2

alaraja = 0
while not pienin_ratkaistu:
    hakuaika = alaraja + (pienin_voitto - alaraja) // 2
    if voitto(hakuaika):
        pienin_voitto = hakuaika
        if not voitto(hakuaika - 1):
            pienin_ratkaistu = True
    else:
        alaraja = hakuaika

print(f"Alaraja löytyi: {pienin_voitto}")

ylaraja = aika
while not suurin_ratkaistu:
    hakuaika = suurin_voitto + (ylaraja - suurin_voitto) // 2
    if voitto(hakuaika):
        suurin_voitto = hakuaika
        if not voitto(hakuaika + 1):
            suurin_ratkaistu = True
    else:
        ylaraja = hakuaika

print(f"Yläraja löytyi: {suurin_voitto}")

print(f"Vastaus on {suurin_voitto} - {pienin_voitto} + 1 = {suurin_voitto-pienin_voitto+1}")
