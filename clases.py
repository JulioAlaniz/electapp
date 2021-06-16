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
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown

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
        print('Para colaborar con el desarrollo de esta aplicación, ingresá al enlace siguiente.')
        print('https://cafecito.app/julio-58')
        print('gracias!')
        print('\n\n\n\n\n')
        sys.exit()

console = Console()

cablesMenu = [
    {"indice":"1", "tipo":"Cable unipolar"},
    {"indice":"2", "tipo":"Cable tipo taller"},
    {"indice":"3", "tipo":"Cable subterraneo unipolar en bandeja"},
    {"indice":"4", "tipo":"Cable subterraneo unipolar enterrado"},
    {"indice":"5", "tipo":"Cable subterraneo bipolar en bandeja"},
    {"indice":"6", "tipo":"Cable subterraneo bipolar enterrado"},
    {"indice":"7", "tipo":"Cable subterraneo tripolar c/s neutro en bandeja"},
    {"indice":"8", "tipo":"Cable subterraneo tripolar c/s neutro enterrado"},
    {"indice":"9", "tipo":"Para salir"}
]

def formatPantalla():
    console.print(Markdown('# Opciones de cables'))
    table = Table(show_header=True, header_style="bold steel_blue1")
    table.add_column("Indice", style="dim", width=30, justify="center")
    table.add_column("Tipo de cable", style="dim", width=120, justify="left")
    i=0
    for i in range(0,len(cablesMenu)):
        elementos=cablesMenu[i]
        indice = elementos["indice"]
        tipo = elementos["tipo"]
        table.add_row(f"{indice}", f"{tipo}")
    console.print(table)

# *************************** Clases ***************************

class Menu:
    def __menu__(self):
        i = 0
        while i == 0:
  #          borrarPantalla()
 #           formatSalida()
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
