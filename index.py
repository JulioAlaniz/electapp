from unipolar import calcularCorrienteUnipolar, borrarPantalla
from taller import calcularCorrienteTaller
from subterraneo import calcularCorrienteSubtUnipolarB
from subterraneo import calcularCorrienteSubtUnipolarE
from subterraneo import calcularCorrienteSubtBipolarB
from subterraneo import calcularCorrienteSubtBipolarE
from subterraneo import calcularCorrienteSubtTripolarB
from subterraneo import calcularCorrienteSubtTripolarE
opcion=[1,2,3,4,5,6,7,8,9]
salir = [0,1]
i = 0

while i in salir:
    if i == 0:
        try:
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
            print()
            o = int(input('ingrese opcion (de 1 a 9)\n'))
            if o == 1:
                calcularCorrienteUnipolar()
                a = int(input('1: salir de la app ó 0: elegir otro cable\n'))
                i = salir[a]
            elif o == 2:
                calcularCorrienteTaller()
                a = int(input(' 1: salir de la app ó 0: elegir otro cable\n'))
                i = salir[a]
            elif o == 3:
                calcularCorrienteSubtUnipolarB()
                a = int(input('1: salir de la app ó 0: elegir otra opcion\n'))
                i = salir[a]
            elif o == 4:
                calcularCorrienteSubtUnipolarE()
                a = int(input('1: salir de la app ó 0: elegir otra opcion\n'))
                i = salir[a]
            elif o == 5:
                calcularCorrienteSubtBipolarB()
                a = int(input('1: salir de la app ó 0: elegir otra opcion\n'))
                i = salir[a]
            elif o == 6:
                calcularCorrienteSubtBipolarB()
                a = int(input('1: salir de la app ó 0: elegir otra opcion\n'))
                i = salir[a]
            elif o == 7:
                calcularCorrienteSubtTripolarB()
                a = int(input('1: salir de la app ó 0: elegir otra opcion\n'))
                i = salir[a]
            elif o == 8:
                calcularCorrienteSubtTripolarE()
                a = int(input('1: salir de la app ó 0: elegir otra opcion\n'))
                i = salir[a]
            else:
                print('El dato ingresado esta fuera de rango')
        except:
            print('ups! Volve a intentarlo')
    else:
        borrarPantalla()
        print('\n\n\n\n\n\ngracias por usar electapp')
        print('https://github.com/JulioAlaniz')
        print('\n\n\n\n\n')
        break
