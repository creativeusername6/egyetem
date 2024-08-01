beolvas = []
ossz = 0
with open("lista.txt", "r", encoding="utf-8") as f:
    for adat in f:
        adat = adat.strip().split()
        ossz += 1
        for adat2 in adat:
            beolvas.append(adat2)

elofordulas = {}
for adat in beolvas:
    if adat not in elofordulas:
        elofordulas[adat] = 1
    else:
        elofordulas[adat] += 1

for elofor, ertek in elofordulas.items():
    print(f"{elofor}: {round((ertek * 100) / ossz)}%")