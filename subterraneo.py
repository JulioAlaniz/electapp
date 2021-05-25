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

def calcularSecionUnipolarB(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtUnipolarB[arg]:.2f}"),' Amp')
    print('')

def calcularCorrienteSubtUnipolarB():
    salir = [0,1]
    i = 0
    while i in salir:
        
        if i == 0:
            try:
                watts =float(input('ingrese la carga en watts\n'))
                volts = 220.0
                amps = watts/volts
                if amps<=41:#1
                    calcularSecionUnipolarB(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>41 and amps<=53:#2
                    calcularSecionUnipolarB(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>53 and amps<=80:#3
                    calcularSecionUnipolarB(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>80 and amps<=97:#4
                    calcularSecionUnipolarB(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>97 and amps<=121:#5
                    calcularSecionUnipolarB(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>121 and amps<=149:#6
                    calcularSecionUnipolarB(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>149 and amps<=181:#7
                    calcularSecionUnipolarB(8)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>181 and amps<=221:#8
                    calcularSecionUnipolarB(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>221 and amps<=272:#9
                    calcularSecionUnipolarB(10)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>272 and amps<=316:#10
                    calcularSecionUnipolarB(11)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>316 and amps<=360:#11
                    calcularSecionUnipolarB(12)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>360 and amps<=410:#12
                    calcularSecionUnipolarB(13)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break

# ****************** Unipolar E (enterrado) ******************************

def calcularSecionUnipolarE(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtUnipolarE[arg]:.2f}"),' Amp')
    print('')

def calcularCorrienteSubtUnipolarE():
    salir = [0,1]
    i = 0
    while i in salir:
        
        if i == 0:
            try:
                watts =float(input('ingrese la carga en watts\n'))
                volts = 220.0
                amps = watts/volts
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

def calcularCorrienteSubtBipolarB():
    salir = [0,1]
    i = 0
    while i in salir:
        
        if i == 0:
            try:
                watts =float(input('ingrese la carga en watts\n'))
                volts = 220.0
                amps = watts/volts
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

def calcularSecionBipolarE(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtBipolarE[arg]:.2f}"),' Amp')
    print('')

def calcularCorrienteSubtBipolarE():
    salir = [0,1]
    i = 0
    while i in salir:
        
        if i == 0:
            try:
                watts =float(input('ingrese la carga en watts\n'))
                volts = 220.0
                amps = watts/volts
                if amps<=28:#1
                    calcularSecionBipolarE(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>28 and amps<=38:#2
                    calcularSecionBipolarE(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>38 and amps<=50:#3
                    calcularSecionUnipolarE(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>50 and amps<=66:#4
                    calcularSecionUnipolarE(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>66 and amps<=89:#5
                    calcularSecionUnipolarE(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>89 and amps<=110:#6
                    calcularSecionUnipolarE(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:

            break       


# ****************** Tripolar B (en bandeja) ******************************

def calcularSecionTripolarB(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtTripolarB[arg]:.2f}"),' Amp')
    print('')

def calcularCorrienteSubtTripolarB():
    salir = [0,1]
    i = 0
    while i in salir:
        
        if i == 0:
            try:
                watts =float(input('ingrese la carga en watts\n'))
                volts = 220.0
                amps = watts/volts
                if amps<=15:#1
                    calcularSecionTripolarB(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>15 and amps<=21:#2
                    calcularSecionTripolarB(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>21 and amps<=28:#3
                    calcularSecionTripolarB(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>28 and amps<=37:#4
                    calcularSecionTripolarB(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>37 and amps<=50:#5
                    calcularSecionTripolarB(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>50 and amps<=64:#6
                    calcularSecionTripolarB(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>64 and amps<=86:#7
                    calcularSecionTripolarB(8)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>86 and amps<105:#8
                    calcularSecionTripolarB(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>105 and amps<128:#8
                    calcularSecionTripolarB(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break


# ****************** Tripolar E (enterrado) ******************************

def calcularSecionTripolarE(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxSubtTripolarE[arg]:.2f}"),' Amp')
    print('')

def calcularCorrienteSubtTripolarE():
    salir = [0,1]
    i = 0
    while i in salir:
        
        if i == 0:
            try:
                watts =float(input('ingrese la carga en watts\n'))
                volts = 220.0
                amps = watts/volts
                if amps<24:#1
                    calcularSecionTripolarE(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>24 and amps<=32:#2
                    calcularSecionTripolarE(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>32 and amps<=44:#3
                    calcularSecionTripolarE(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>44 and amps<=56:#4
                    calcularSecionTripolarE(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>56 and amps<=72:#5
                    calcularSecionTripolarE(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>72 and amps<=94:#6
                    calcularSecionTripolarE(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>94 and amps<=120:#7
                    calcularSecionTripolarE(8)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>120 and amps<=144:#8
                    calcularSecionTripolarE(9)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>144 and amps<=172:#9
                    calcularSecionTripolarE(10)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break
