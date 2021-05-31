# *************************** imports *****************************
from subterraneo import opcionCorrienteSubtUnipolarB
from unipolar import opcionCorrienteUnipolar
from taller import opcionCorrienteTaller
from subterraneo import opcionCorrienteSubtUnipolarE
from subterraneo import opcionCorrienteSubtBipolarB
from subterraneo import opcionCorrienteSubtBipolarE
from subterraneo import opcionCorrienteSubtTripolarB
from subterraneo import opcionCorrienteSubtTripolarE
import sys

# *************************** Funsiones ***************************
import os
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def salir(dato):
    if dato == 9:
        borrarPantalla()
        print('\n\n\n\n\n\ngracias por usar electapp')
        print('https://github.com/JulioAlaniz')
        print('\n\n\n\n\n')
        sys.exit()

# *************************** Clases ***************************

class Menu:
    def __init__(self):
        self.opcion=[1,2,3,4,5,6,7,8,9]
        
    def menu(self):
        borrarPantalla()
        print("*************** Opciones de cables ********************")
        print("1-> Cable unipolar")
        print("2-> Cable tipo taller")
        print("3-> Cable subterraneo unipolar en bandeja")
        print("4-> Cable subterraneo unipolar enterrado")
        print("5-> Cable subterraneo bipolar en bandeja")
        print("6-> Cable subterraneo bipolar enterrado")
        print("7-> Cable subterraneo tripolares c/s neutro en bandeja")
        print("8-> Cable subterraneo tripolares c/s neutro enterrado")
        print("9-> Para salir")
        print()
        opcion = int(input('ingrese opcion (de 1 a 9)\n'))
        return(opcion)
       
 


class TipoCable:
    def __init__(self, opcionCable, arg):
        if opcionCable == 1:
            opcionCorrienteUnipolar(arg)
        elif opcionCable ==2:
            opcionCorrienteTaller(arg)
        elif opcionCable ==3:
            opcionCorrienteSubtUnipolarB(arg)
        elif opcionCable ==4:
            opcionCorrienteSubtUnipolarE(arg)
        elif opcionCable ==5:
            opcionCorrienteSubtBipolarB(arg)
        elif opcionCable ==6:
            opcionCorrienteSubtBipolarE(arg)
        elif opcionCable ==7:
            opcionCorrienteSubtTripolarB(arg)
        elif opcionCable ==8:
            opcionCorrienteSubtTripolarE(arg)


class CalculoCorriente:
    def __init__(self):
        self.watts =float(input('ingrese la carga en watts\n'))
        self.volts =float(input('ingrese el voltaje\n'))

    def amperios(self):
        amps=self.watts/self.volts
        print(amps)     # agregar formateo para dos digitos
        return amps
    #borrarPantalla()
    #print('la seccion nominal unipolable en amperios es de:\t'+ str(f"{corrienteMax[arg]:.2f}"),' Amp')
    #print('fusible NH es de:\t\t\t\t'+ str(f"{fusible[arg]:.2f}"),' Amp')
    #print('')   
    #pass
