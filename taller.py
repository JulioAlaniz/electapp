#electapp v0.2
#calculo de secciones de cable en extraido de la tabla de argenplas

#*************Listas cable tipo taller*************
seccionTaller=[0.75,1.0,1.50,2.50,4.0,6.0,10.0,16.0,]
corrienteMaxTaller=[10.0,13.0,16.0,22.0,30.0,38.0,53.0,71.0]



#***************funciones***************
import os
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def calcularSeccionTaller(arg):
    borrarPantalla()
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccionTaller[arg]:.2f}"),' mm2')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMaxTaller[arg]:.2f}"),' Amp')
    print('')

def calcularCorrienteTaller():
    salir = [0,1]
    i = 0
    while i in salir:
        if i == 0:
            try:
                watts =float(input('ingrese la carga en watts\n'))
                volts = 220.0
                amps = watts/volts
                if amps <=10:#1
                    calcularSeccionTaller(0)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>10 and amps<=13:#2
                    calcularSeccionTaller(1)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>13 and amps<=16:#3
                    calcularSeccionTaller(2)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>16 and amps<=22:#4
                    calcularSeccionTaller(3)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>22 and amps<=30:#5
                    calcularSeccionTaller(4)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>30 and amps<=38:#6
                    calcularSeccionTaller(5)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>38 and amps<=53:#7
                    calcularSeccionTaller(6)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                elif amps>53 and amps<=71:#8
                    calcularSeccionTaller(7)
                    a = int(input('1: elegir otro cable ó 0: mismo cable\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:
            break

