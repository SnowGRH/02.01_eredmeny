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

def jatekos_vesztett_teszt():
    jLapok =[10,5,6]
    gLapok = [2,7]
    kapott = eredmeny(jLapok,gLapok)
    vart ="jatekos_vesztett_teszt"
    if kapott == vart:
        print( "A teszt sikeres")
    else:
        print( "A teszt megbukott")
def tesztek():
    jatekos_vesztett_teszt()


tesztek()