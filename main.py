from clases import CalculoCorriente, TipoCable
from clases import Menu
from clases import salir


opcion=Menu()
opcionCable=opcion.menu()
print("la opcion elegida es:", opcionCable, '\n')
salir(opcionCable)
corriente=CalculoCorriente()
amps=corriente.amperios()
cable=TipoCable(opcionCable, amps)
    

