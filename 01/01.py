import string

arvot = []
with open("input.txt") as f:
    for r in f:
        r = r.strip()
        print(r)
        for c in r:
            if c in string.digits:
                arvo = int(c) * 10
                break
        for c in r[::-1]:
            if c in string.digits:
                arvo += int(c)
                break
        print(arvo)
        arvot.append(arvo)

print(sum(arvot))
