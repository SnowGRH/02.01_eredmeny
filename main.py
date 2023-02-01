#megoldas
def eredmeny( jPontja: list[int] , gPontja: list[int] ):
    if pOsszeg(jPontja) > 21:
        return "Játékos vesztett"
    elif pOsszeg(gPontja) > 21:
        return "Játékos vesztett"

def pOsszeg(lista: list[int]):
    i = 0
    pontosszeg = 0
    while i < len(lista):
        pontosszeg += lista[i]
        i += 1
    return pontosszeg
#tesztek