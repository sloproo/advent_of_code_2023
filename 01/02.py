import string

arvot = []
luvut = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open("input.txt") as f:
    for r in f:
        r = r.strip()
        arvo = 0
        for i in range(len(r)):
            if r[i] in string.digits:
                arvo = int(r[i]) * 10
                break
            for j in [3, 4, 5]:
                if r[i:i+j] in luvut:
                    arvo += luvut[r[i:i+j]] * 10
                    break
            if arvo != 0:
                break


        for i in range(len(r))[::-1]:
            if r[i] in string.digits:
                arvo += int(r[i])
                break
            for j in [3, 4, 5]:
                if r[i:i+j] in luvut:
                    arvo += luvut[r[i:i+j]]
                    break
            if arvo %10 != 0:
                break

        print(arvo)
        arvot.append(arvo)

print(sum(arvot))
