from unipolar import calcularCorrienteUnipolar, borrarPantalla
from taller import calcularCorrienteTaller


opcion=[1,2,3,4,5,6,7,8,9]
salir = [0,1]
i = 0

while i in salir:
    if i == 0:
        try:
            o = int(input('ingrese opcion\n'))
            if o == 1:
                calcularCorrienteUnipolar()
                a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                i = salir[a]
            elif o == 2:
                calcularCorrienteTaller()
                a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                i = salir[a]
            else:
                print('El dato ingresado esta fuera de rango')
        except:
            print('ups! Volve a intentarlo')
            #break
    else:
        borrarPantalla()
        print('\n\n\n\n\n\ngracias por usar electapp')
        print('https://github.com/JulioAlaniz')
        print('\n\n\n\n\n')
        break
