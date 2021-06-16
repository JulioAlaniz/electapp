from clases import CalculoCorriente, TipoCable, borrarPantalla, formatPantalla
from clases import Menu
from clases import salir

i = 0
while i == 0:
    borrarPantalla()
    formatPantalla()
    opcion = Menu()
    opcionCable = opcion.__menu__()
    borrarPantalla()
    print("la opcion elegida es:", opcionCable, "\n")
    print("la tensión de cálculo es de 220v\n")
    salir(opcionCable)
    corriente = CalculoCorriente()
    amps = corriente.amperios()
    cable = TipoCable(opcionCable, amps)
else:
    input("presione para continuar")
