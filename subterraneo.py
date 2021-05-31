#electapp v0.2
#calculo de secciones de cable en extraido de la tabla de argenplas

#************* Listas cable tipo subterraneo *************

from taller import borrarPantalla


seccion=[1.50,2.50,4.0,6.0,10.0,16.0,25.0,35.0,50.0,70.0,95.0,120.0,150.0,185.0]
corrienteMaxSubtUnipolarB=[0.0,0.0,41.0,53.0,80.0,97.0,121.0,149.0,181.0,221.0,272.0,316.0,360.0,410.0]
corrienteMaxSubtUnipolarE=[0.0,0.0,54.0,68.0,89.0,116.0,148.0,177.0,209.0,258.0,307.0,349.0,390.0,440.0]
corrienteMaxSubtBipolarB=[0.0,0.0,19.0,26.0,35.0,44.0,61.0,82.0]
corrienteMaxSubtBipolarE=[0.0,0.0,28.0,38.0,50.0,66.0,89.0,110.0]
corrienteMaxSubtTripolarB=[0.0,0.0,15.0,21.0,28.0,37.0,50.0,64.0,86.0,105.0,128.0]
corrienteMaxSubtTripolarE=[0.0,0.0,24.0,32.0,44.0,56.0,72.0,94.0,120.0,144.0,182.0]

# *************** Unipolar B (en bandeja) *******************************************************

def calcularSeccionUnipolarB(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtUnipolarB[arg]:.2f}"),' Amp')
    print('')

def opcionCorrienteSubtUnipolarB(amps):
    salir = [0,1]
    i = 0
    while i in salir:
        if i == 0:
            try:
                if amps<=41:#1
                    calcularSeccionUnipolarB(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>41 and amps<=53:#2
                    calcularSeccionUnipolarB(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>53 and amps<=80:#3
                    calcularSeccionUnipolarB(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>80 and amps<=97:#4
                    calcularSeccionUnipolarB(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>97 and amps<=121:#5
                    calcularSeccionUnipolarB(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>121 and amps<=149:#6
                    calcularSeccionUnipolarB(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>149 and amps<=181:#7
                    calcularSeccionUnipolarB(8)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>181 and amps<=221:#8
                    calcularSeccionUnipolarB(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>221 and amps<=272:#9
                    calcularSeccionUnipolarB(10)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>272 and amps<=316:#10
                    calcularSeccionUnipolarB(11)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>316 and amps<=360:#11
                    calcularSeccionUnipolarB(12)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>360 and amps<=410:#12
                    calcularSeccionUnipolarB(13)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break


# *************** Unipolar e (enterrado) *******************************************************

def calcularSecionUnipolarE(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtUnipolarE[arg]:.2f}"),' Amp')
    print('')

def opcionCorrienteSubtUnipolarE(amps):
    salir = [0,1]
    i = 0
    while i in salir:
        if i == 0:
            try:
                if amps<=54:#1
                    calcularSecionUnipolarE(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>54 and amps<=68:#2
                    calcularSecionUnipolarE(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>68 and amps<=89:#3
                    calcularSecionUnipolarE(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>89 and amps<=116:#4
                    calcularSecionUnipolarE(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>116 and amps<=148:#5
                    calcularSecionUnipolarE(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>148 and amps<=177:#6
                    calcularSecionUnipolarE(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>177 and amps<=209:#7
                    calcularSecionUnipolarE(8)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>209 and amps<=258:#8
                    calcularSecionUnipolarE(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>258 and amps<=307:
                    calcularSecionUnipolarE(11)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>307 and amps<=349:#11
                    calcularSecionUnipolarE(12)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>349 and amps<=390:#12
                    calcularSecionUnipolarE(13)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>390 and amps<=440:#12
                    calcularSecionUnipolarE(13)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break

# ******************* Bipolar B (en bandeja)***********************************

def calcularSecionBipolarB(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtBipolarB[arg]:.2f}"),' Amp')
    print('')

def opcionCorrienteSubtBipolarB(amps):
    salir = [0,1]
    i = 0
    while i in salir:
        if i == 0:
            try:
                if amps<=19:#1
                    calcularSecionBipolarB(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>19 and amps<=26:#2
                    calcularSecionBipolarB(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>26 and amps<=35:#3
                    calcularSecionBipolarB(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>35 and amps<=44:#4
                    calcularSecionBipolarB(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>44 and amps<=61:#5
                    calcularSecionBipolarB(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>61 and amps<=82:#6
                    calcularSecionBipolarB(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break       

# ****************** Bipolar E (enterrado) ******************************

def calcularSeccionBipolarE(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtBipolarE[arg]:.2f}"),' Amp')
    print('')

def opcionCorrienteSubtBipolarE(amps):
    salir = [0,1]
    i = 0
    while i in salir:
        if i == 0:
            try:
                if amps<=28:#1
                    calcularSeccionBipolarE(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>28 and amps<=38:#2
                    calcularSeccionBipolarE(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>38 and amps<=50:#3
                    calcularSeccionBipolarE(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>50 and amps<=66:#4
                    calcularSeccionBipolarE(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>66 and amps<=89:#5
                    calcularSeccionBipolarE(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>89 and amps<=110:#6
                    calcularSeccionBipolarE(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break       

# ****************** Tripolar B (en bandeja) ******************************

def calcularSeccionTripolarB(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtTripolarB[arg]:.2f}"),' Amp')
    print('')

def opcionCorrienteSubtTripolarB(amps):
    salir = [0,1]
    i = 0
    while i in salir:
        if i == 0:
            try:
                if amps<=15:#1
                    calcularSeccionTripolarB(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>15 and amps<=21:#2
                    calcularSeccionTripolarB(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>21 and amps<=28:#3
                    calcularSeccionTripolarB(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>28 and amps<=37:#4
                    calcularSeccionTripolarB(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>37 and amps<=50:#5
                    calcularSeccionTripolarB(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>50 and amps<=64:#6
                    calcularSeccionTripolarB(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>64 and amps<=86:#7
                    calcularSeccionTripolarB(8)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>86 and amps<105:#8
                    calcularSeccionTripolarB(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>105 and amps<128:#8
                    calcularSeccionTripolarB(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break


# ****************** Tripolar E (enterrado) ******************************

def calcularSeccionTripolarE(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtTripolarE[arg]:.2f}"),' Amp')
    print('')

def opcionCorrienteSubtTripolarE(amps):
    salir = [0,1]
    i = 0
    while i in salir:
        
        if i == 0:
            try:
                if amps<24:#1
                    calcularSeccionTripolarE(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>24 and amps<=32:#2
                    calcularSeccionTripolarE(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>32 and amps<=44:#3
                    calcularSeccionTripolarE(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>44 and amps<=56:#4
                    calcularSeccionTripolarE(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>56 and amps<=72:#5
                    calcularSeccionTripolarE(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>72 and amps<=94:#6
                    calcularSeccionTripolarE(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>94 and amps<=120:#7
                    calcularSeccionTripolarE(8)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>120 and amps<=144:#8
                    calcularSeccionTripolarE(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>144 and amps<=172:#9
                    calcularSeccionTripolarE(10)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break
