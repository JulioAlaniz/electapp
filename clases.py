#electapp v0.2
#calculo de secciones de cable en extraido de la tabla de argenplas



class menu():
    def __init__(self):
        opcionCables=[1,2,3,4,5,6,7,8,9]
        salir = [0,1]
        
    def menu():
        while i in salir:
            if i == 0:
                try:
                    print("")
                    print("*************** Opciones de cables ********************")
                    print("")
                    print("1-> Cable unipolar")
                    print("2-> Cable tipo taller")
                    print("3-> Cable subterraneo unipolar en bandeja")
                    print("4-> Cable subterraneo unipolar enterrado")
                    print("6-> Cable subterraneo bipolar en bandeja")
                    print("7-> Cable subterraneo bipolar enterrado")
                    print("8-> Cable subterraneo tripolares c/s neutro en bandeja")
                    print("9-> Cable subterraneo tripolares c/s neutro enterrado")
                    print("")
                    o = int(input('ingrese opcion\n'))
                    if o == 1:
                        calcularCorrienteUnipolar()
                        a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                        i = salir[a]
                    elif o == 2:
                        calcularCorrienteTaller()
                        a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                        i = salir[a]
                    elif o == 3:
                        calcularCorrienteSubterraneoUnipolarB()
                        a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                        i = salir[a]
                    elif o == 4:
                        calcularCorrienteSubterraneoUnipolarE()
                        a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                        i = salir[a]
                    elif o == 5:
                        calcularCorrienteSubterraneoBipolarB()
                        a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                        i = salir[a]
                    elif o == 6:
                        calcularCorrienteSubterraneoBipolarE()
                        a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                        i = salir[a]
                    elif o == 7:
                        calcularCorrienteSubterraneoTripolarB()
                        a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                        i = salir[a]
                    elif o == 8:
                        calcularCorrienteSubterraneoTripolar()
                        a = int(input('desea continuar, 1: salir ó 0: elegir otra opcion\n'))
                        i = salir[a]
                    elif o == 9:
                        calcularCorrienteSubterraneoUnipolar()
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
    

class cable():
    pass

class unipolar(cable):
    pass

class taller(cable):
    pass

class subterraneo(cable):
    pass