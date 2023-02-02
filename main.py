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

def jatekos_vesztett_teszt1():
    jLapok =[10,5,6]
    gLapok = [2,7]
    kapott = eredmeny(jLapok,gLapok)
    vart ="jatekos_vesztett_teszt"
    if kapott == vart:
        print( "jatekos_vesztett_teszt1 sikeres")
    else:
        print( "jatekos_vesztett_teszt1 megbukott")

def jatekos_vesztett_teszt2():
    jLapok =[10,3,11]
    gLapok = [5,11]
    kapott = eredmeny(jLapok,gLapok)
    vart ="jatekos_vesztett_tulocsrult_teszt"
    if kapott == vart:
        print( "jatekos_vesztett_teszt2 sikeres")
    else:
        print( "jatekos_vesztett_teszt2 megbukott")
def jatekos_vesztett_teszt3():
    jLapok =[5,6]
    gLapok = [6,10]
    kapott = eredmeny(jLapok,gLapok)
    vart ="jatekos_vesztett_magasab_teszt"
    if kapott == vart:
        print( "jatekos_vesztett_teszt3 sikeres")
    else:
        print( "jatekos_vesztett_teszt3 megbukott")
def gep_vesztett_teszt1():
    jLapok =[10,11]
    gLapok = [8,5,6]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Gep_vesztett_21j_teszt"
    if kapott == vart:
        print( "Gep_vesztett_teszt1 sikeres")
    else:
        print( "Gep_vesztett_teszt1 megbukott")

def gep_vesztett_teszt2():
    jLapok =[10,5]
    gLapok = [8,5]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Gep_vesztett_kissebbbbb_teszt"
    if kapott == vart:
        print( "Gep_vesztett_teszt2 sikeres")
    else:
        print( "Gep_vesztett_teszt2 megbukott")


def gep_vesztett_teszt3():
    jLapok =[10,8]
    gLapok = [8,10,10]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Gep_vesztett_tulcsordult_teszt"
    if kapott == vart:
        print( "Gep_vesztett_teszt3 sikeres")
    else:
        print( "Gep_vesztett_teszt3 megbukott")

def dontetlen_teszt1():
    jLapok =[11,11]
    gLapok = [11,11]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Gep_vesztett_tulcsordult_teszt"
    if kapott == vart:
        print( "dontetlen_teszt3 sikeres")
    else:
        print( "dontetlen_teszt3 megbukott")
def dontetlen_teszt2():
    jLapok =[10,10]
    gLapok = [10,10]
    kapott = eredmeny(jLapok,gLapok)
    vart ="dontetlen_teszt"
    if kapott == vart:
        print( "dontetlen_teszt3 sikeres")
    else:
        print( "dontetlen_teszt3 megbukott")
def tesztek():
    jatekos_vesztett_teszt1()
    jatekos_vesztett_teszt2()
    jatekos_vesztett_teszt3()
    gep_vesztett_teszt1()
    gep_vesztett_teszt2()
    gep_vesztett_teszt3()
    dontetlen_teszt1()
    dontetlen_teszt2()


tesztek()