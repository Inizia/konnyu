import random
lista = []
def general():
    i = 0
    szam = 0
    while i < 13:
        szam = int(random.random() * 111) + 40
        while szam % 2 == 0:
            szam = int(random.random() * 111) + 40
        lista.append(szam)
        i += 1

    return lista


def ketjegyu():
    i = 0
    darab = 0
    while i < len(lista):
        if lista[i] > 9:
            darab += 1
        i += 1

    return darab


def sorozat_csillag():
    szoveg = ""
    i = 0
    while i < len(lista):
        if i < len(lista) -1:
            szoveg += str(lista[i]) + "* "
        else:
            szoveg += str(lista[i])
        i += 1

    return szoveg


def fajlba_ir():
    fajl = open("ketjegyu.txt", "w", encoding="utf-8")
    fajl.write(f"Kétjegyűek száma:{ketjegyu()}")
    fajl.close()