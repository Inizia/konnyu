bekert_szamok = []

def szambeker():
    print("I/a,b:")
    szam1 = int(input("\t Adja meg a(z) 1. negatív egész számot: "))
    while not szam1 < 0:
        szam1 = int(input("\t Adja meg újra a(z) 1. negatív egész számot: "))

    szam2 = int(input("\t Adja meg a(z) 2. negatív egész számot: "))
    while not szam2 < 0:
        szam2 = int(input("\t Adja meg újra a(z) 2. negatív egész számot: "))

    szam3 = int(input("\t Adja meg a(z) 3. negatív egész számot: "))
    while not szam3 < 0:
        szam3 = int(input("\t Adja meg újra a(z) 3. negatív egész számot: "))


    bekert_szamok.append(szam1)
    bekert_szamok.append(szam2)
    bekert_szamok.append(szam3)


def negyzet():
    i = 0
    negyzet_szam = 0
    indx = 0
    while i < len(bekert_szamok):
        if (bekert_szamok[i] * bekert_szamok[i]) < negyzet_szam:
            negyzet_szam = bekert_szamok[i] * bekert_szamok[i]
            indx = i
        i += 1

    legkissebb = bekert_szamok[indx]
    hely = indx + 1

    print(f"I/c: \n \t A legkisebb négyzetű szám: {legkissebb}, megadási sorrendje: {hely}")



