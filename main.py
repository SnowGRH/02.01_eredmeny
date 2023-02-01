#megoldas
def eredmeny(jatokosPontja,gepPontja):
    if pOsszeg(jatokosPontja) > 21:
        return "Játékos nyert"
    elif pOsszeg(gepPontja) > 21:
        return "Játékos vesztet"

def pOsszeg(lista):
    i = 0
    pontosszeg = 0
    while i < len(lista):
        pontosszeg += lista[i]
        i+=1
    return pontosszeg
#tesztek