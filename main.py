#megoldas
def eredmeny( jPontja: list[int] , gPontja: list[int] ):
    jPont = pOsszeg(jPontja)
    gPont = pOsszeg(gPontja)
    jLap = len(jPontja)
    gLap = len(gPontja)
    ki = ""

    if (jPont <= 21) and (gPont <= 21):
        if gPont < jPont:
            ki = "Gép vesztett"
        elif jPont > gPont:
            ki = "Játékos vesztett"
        elif jPont == gPont:
            if jLap > gLap:
                ki = "Játékos vesztett"
            elif jLap < gLap:
                ki= "Gép vesztett"
            else:
                ki = "Döntetlen"
    else:
        if gPont > 21:
            ki = "Gép vesztett"
        elif jPont >21:
            ki = "Játékos vesztett"
        elif jPont > 21 and gPont > 21:
            ki = "Döntetlen"
    return ki



def pOsszeg(lista: list[int]):
    i = 0
    pontosszeg = 0
    while i < len(lista):
        pontosszeg += lista[i]
        i += 1
    return pontosszeg
#tesztek

def jatekos_vesztett_teszt1():
    jLapok =[10,6,6]
    gLapok = [2,7]
    kapott = eredmeny(jLapok,gLapok)
    vart = "Játékos vesztett"
    if kapott == vart:
        print( "jatekos_vesztett_teszt1 sikeres")
    else:
        print( "jatekos_vesztett_teszt1 megbukott")

def jatekos_vesztett_teszt2():
    jLapok =[10,3,11]
    gLapok = [5,11]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Játékos vesztett"
    if kapott == vart:
        print( "jatekos_vesztett_teszt2 sikeres")
    else:
        print( "jatekos_vesztett_teszt2 megbukott")
def jatekos_vesztett_teszt3():
    jLapok =[5,6]
    gLapok = [6,10]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Játékos vesztett"
    if kapott == vart:
        print( "jatekos_vesztett_teszt3 sikeres")
    else:
        print( "jatekos_vesztett_teszt3 megbukott")
def gep_vesztett_teszt1():
    jLapok =[10,11]
    gLapok = [8,5,6]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Gép vesztett"
    if kapott == vart:
        print( "Gep_vesztett_teszt1 sikeres")
    else:
        print( "Gep_vesztett_teszt1 megbukott")

def gep_vesztett_teszt2():
    jLapok =[10,5]
    gLapok = [8,5]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Gép vesztett"
    if kapott == vart:
        print( "Gep_vesztett_teszt2 sikeres")
    else:
        print( "Gep_vesztett_teszt2 megbukott")


def gep_vesztett_teszt3():
    jLapok =[10,8]
    gLapok = [8,10,10]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Gép vesztett"
    if kapott == vart:
        print( "Gep_vesztett_teszt3 sikeres")
    else:
        print( "Gep_vesztett_teszt3 megbukott")

def dontetlen_teszt1():
    jLapok =[11,11]
    gLapok = [11,11]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Döntetlen"
    if kapott == vart:
        print( "dontetlen_teszt3 sikeres")
    else:
        print( "dontetlen_teszt3 megbukott")
def dontetlen_teszt2():
    jLapok =[10,10]
    gLapok = [10,10]
    kapott = eredmeny(jLapok,gLapok)
    vart ="Döntetlen"
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