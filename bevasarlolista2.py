from itertools import combinations

def a(b, c):
    return list(combinations(b, c))

if __name__ == "__main__":
    beolvas = []
    termek = []
    osszes = []
    ossz = 0
    with open("lista.txt", "r", encoding="utf-8") as f:
        for adat in f:
            adat = adat.strip().split()
            beolvas.append(adat)
            ossz += 1
            for adat2 in adat:
                if adat2 not in termek:
                    termek.append(adat2)

    comb = ossz
    while comb > 0:
        osszes.extend(a(termek, comb))
        comb -= 1

    osszes = tuple(osszes)
    beolvas = tuple(tuple(adat) for adat in beolvas)

    elofordulas = {}
    for adat in osszes:
        if adat not in elofordulas:
            elofordulas[adat] = 0

    for adat in beolvas:
        if adat in elofordulas:
            elofordulas[adat] += 1

    for elofor, ertek in elofordulas.items():
        print(f"{elofor}: {ertek}")