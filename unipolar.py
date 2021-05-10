#electapp v0.2
#calculo de secciones de cable en extraido de la tabla de argenplas
#************Listas cable unipolar*************
seccion=[0.50,0.75,1.0,1.50,2.50,4.0,6.0,10.0,16.0,25.0,35.0,50.0,70.0,95.0,120.0,150.0,185.0]
diametroExterior=[2.15,2.3,2.7,3.0,3.65,4.3,4.8,6.3,7.7,9.9,11.1,12.9,15.55,17.2,19.1,21.8]
peso=[0.89,1.14,1.57,2.09,3.32,5.0,6.80,11.9,17.9,29.0,39.20,55.4,76.4,98.13,124.9,163.5]
corrienteMax=[3.0,8.0,11.0,13.0,18.0,24.0,31.0,42.0,56.0,73.0,89.0,108.0,136.0,164.0,188.0,310.0]
fusible=[2.0,6.0,10.0,10.0,16.0,20.0,25.0,35.0,50.0,63.0,80.0,100.0,125.0,160.0,160.0,250.0]

#***************funciones***************
import os
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
#borrarPantalla = lambda: os.system ("clear")
	
#borrarPantalla = lambda: os.system ("cls")

#*********
def calcularSeccionUnipolar(arg):
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[arg]:.2f}"),' mm2')
    print('el diametro exterior del cable es de:\t\t'+ str(f"{diametroExterior[arg]:.2f}"),' mm')
    print('el peso por cada 100mts es de:\t\t\t'+ str(f"{peso[arg]:.2f}"),' kg')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMax[arg]:.2f}"),' Amp')
    print('fusible NH es de:\t\t\t\t'+ str(f"{fusible[arg]:.2f}"),' Amp')

def calcularCorrienteUnipolar():
    salir = [0,1]
    i = 0
    while i in salir:
        
        if i == 0:
            try:
                watts =float(input('ingrese la carga en watts\n'))
                volts = 220.0
                amps = watts/volts
                if amps<=3:#1
                    calcularSeccionUnipolar(0)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>3 and amps<=8:#2
                    calcularSeccionUnipolar(1)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>8 and amps<=11:#3
                    calcularSeccionUnipolar(2)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>11 and amps<=13:#4
                    calcularSeccionUnipolar(3)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>13 and amps<=18:#5
                    calcularSeccionUnipolar(4)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>18 and amps<=24:#6
                    calcularSeccionUnipolar(5)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>24 and amps<=31:#7
                    calcularSeccionUnipolar(6)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>31 and amps<=42:#8
                    calcularSeccionUnipolar(7)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>42 and amps<=56:#9
                    calcularSeccionUnipolar(8)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>56 and amps<=73:#10
                    calcularSeccionUnipolar(9)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>73 and amps<=89:#11
                    calcularSeccionUnipolar(10)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>89 and amps<=108:#12
                    calcularSeccionUnipolar(11)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>108 and amps<=136:#13
                    calcularSeccionUnipolar(12)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>136 and amps<=164:#14
                    calcularSeccionUnipolar(13)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>164 and amps<=188:#15
                    calcularSeccionUnipolar(14)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                elif amps>188 and amps<=310:#16
                    calcularSeccionUnipolar(15)
                    a = int(input('desea continuar, 1: elegir otro cable ó 0: continuar\n'))
                    i = salir[a]
                else:
                    print('el dato ingresado está fuera de rango.\n')
            except:
                print('Ups! Volvé a intentarlo')
        else:

            break
             
