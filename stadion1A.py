from Stadion import Stadion
lista = []

def fajl_beolvas():
    fajl = open("stadionok.txt", "r", encoding="utf-8")
    fajl.readline()
    tartalom = fajl.readlines()
    fajl.close()

    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip().strip(";")
        stad = Stadion(sor)
        lista.append(stad)
        i += 1

    print(lista)


def csapatok():
    i = 0
    ny = []
    while i < len(lista):
        if lista[i].varos == "New York":
            ny.append(lista[i].stadion)
            ny.append(lista[i].csapatszam)
        i += 0

    szoveg = ""
    j = 0
    while j < len(ny):
        if j % 2 != 0:
            szoveg += ny[j] + "-"
        else:
            szoveg += (f"{ny[j]}\n)
        j += 1

    return szoveg


