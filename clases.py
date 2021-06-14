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
        print('Para colaborar con el desarrollor de esta aplicación, ingresá al enlace siguiente.')
        print('https://cafecito.app/julio-58')
        print('gracias!')
        print('\n\n\n\n\n')
        sys.exit()

# *************************** Clases ***************************

class Menu:
    def __menu__(self):
        i = 0
        while i == 0:
            borrarPantalla()
            print("*************** Opciones de cables ********************")
            print('')
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
            try:
                opcion = int(input('ingrese opcion (de 1 a 9)\n'))
                if 0 < opcion < 10:
                    return(opcion)
                else:
                    input('la opcion elegida está fuera de rango, vuelva a intentarlo')
            except:
                input('ups! entrada inválida , precione Enter para continuar')
        else:
            input('precione Enter para continuar')
 
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
        i=0
        while i == 0:
            try:
                i = 1
                self.watts =float(input('ingrese la carga en watts\n'))
                self.volts =220 #float(input('ingrese el voltaje\n'))
            except:
                input('entrada inválida, presione culaquier tecla\n')
                i = 0
        else:
            pass

    def amperios(self):
        amps=self.watts/self.volts
        print(amps)     
        return amps
