class Karry:
    def __init__(self, sijainti: tuple, suuntaan: str, ask_eteenp: int, hukka: int, kaydyt: list):
        self.sijainti = sijainti
        self.suuntaan = suuntaan
        self.hukka = hukka
        self.kaydyt = kaydyt

    def __str__(self):
        return (f"sijainti = {self.sijainti}, suuntaan = {self.suuntaan}, hukka = {self.hukka}, käydyt = {self.kaydyt}")
    
    def kaannokset(self) -> list:
        if self.suuntaan[-1] == "U" or self.suuntaan[-1] == "D":
            palautettava = ["L", "R"]
        elif self.suuntaan[-1] == "R" or self.suuntaan[-1] == "L":
            palautettava = ["U", "D"]
        else:
            raise ValueError("Mitä helvettiä olion kääntyessä")
        if len(self.suuntaan) < 3:
            palautettava.append(self.suuntaan[-1])
        return palautettava
    
    def eteneminen(self, suunta: str, kartta: list):
        suunnat = self.kaannokset()
        for suunta in suunnat:
            

    
    def seuraavat(self, kartta: list) -> list:
        seuraavat_suunnat = self.kaannokset()

        

        
    

kartta = []

with open("alku.txt") as f:
    for r in f:
        kartta.append([int(c) for c in r.strip()])

sijainti = (0, 0)
askeleet = ""
hukka = 0
hukkakartta = [[0 for x in range(len(kartta[0]))] for y in range(len(kartta))]

pass

def kelpo(koordinaatit: tuple, kartta:list = kartta) -> bool:
    y, x, = koordinaatit
    if y < 0 or x < 0 or y >= len(kartta) or x >= len(kartta[y]):
        return False
    return True

def liiku(lahto: tuple, suunta: str, pysyvat: tuple = (kartta, askeleet, hukka)) -> tuple:
    kartta, askeleet, hukka = pysyvat
    if suunta == "U":
        kohde = (lahto[0] - 1, lahto[1])
    elif suunta == "R":
        kohde = (lahto[0], lahto[1] + 1)
    elif suunta == "D":
        kohde = (lahto[0] + 1, lahto[1])
    elif suunta == "L":
        kohde = (lahto[0], lahto[1] - 1)
    return (askeleet + suunta, hukka + kartta[kohde[0]][kohde[1]])

def valitse_suunta(lahto: tuple, pysyvat: tuple = (kartta, askeleet, hukka)) -> str:
    pass
