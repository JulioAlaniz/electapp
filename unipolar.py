# electapp v0.2
# calculo de secciones de cable en extraido de la tabla de argenplas
# ************Listas cable unipolar*************
seccion = [
    0.50,
    0.75,
    1.0,
    1.50,
    2.50,
    4.0,
    6.0,
    10.0,
    16.0,
    25.0,
    35.0,
    50.0,
    70.0,
    95.0,
    120.0,
    150.0,
    185.0,
]
diametroExterior = [
    2.15,
    2.3,
    2.7,
    3.0,
    3.65,
    4.3,
    4.8,
    6.3,
    7.7,
    9.9,
    11.1,
    12.9,
    15.55,
    17.2,
    19.1,
    21.8,
]
peso = [
    0.89,
    1.14,
    1.57,
    2.09,
    3.32,
    5.0,
    6.80,
    11.9,
    17.9,
    29.0,
    39.20,
    55.4,
    76.4,
    98.13,
    124.9,
    163.5,
]
corrienteMax = [
    3.0,
    8.0,
    11.0,
    13.0,
    18.0,
    24.0,
    31.0,
    42.0,
    56.0,
    73.0,
    89.0,
    108.0,
    136.0,
    164.0,
    188.0,
    310.0,
]
fusible = [
    2.0,
    6.0,
    10.0,
    10.0,
    16.0,
    20.0,
    25.0,
    35.0,
    50.0,
    63.0,
    80.0,
    100.0,
    125.0,
    160.0,
    160.0,
    250.0,
]

# ***************funciones***************
import os


def borrarPantalla():  # Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


# *********


def calcularSeccionUnipolar(arg):
    borrarPantalla()
    print("************ valores del cable selecionado **************")
    print("")
    print("la seccion nominal es de:\t\t\t" + str(f"{seccion[arg]:.2f}"), " mm2")
    print(
        "el diametro exterior del cable es de:\t\t"
        + str(f"{diametroExterior[arg]:.2f}"),
        " mm",
    )
    print("el peso por cada 100mts es de:\t\t\t" + str(f"{peso[arg]:.2f}"), " kg")
    print(
        "la corriente admisible en amperios es de:\t" + str(f"{corrienteMax[arg]:.2f}"),
        " Amp",
    )
    print("fusible NH es de:\t\t\t\t" + str(f"{fusible[arg]:.2f}"), " Amp")
    print("")
    input("presione cualquier tecla para continuar")


def opcionCorrienteUnipolar(amps):
    if amps <= 3:
        calcularSeccionUnipolar(0)
    elif amps > 3 and amps <= 8:
        calcularSeccionUnipolar(1)
    elif amps > 8 and amps <= 11:
        calcularSeccionUnipolar(2)
    elif amps > 11 and amps <= 13:
        calcularSeccionUnipolar(3)
    elif amps > 13 and amps <= 18:
        calcularSeccionUnipolar(4)
    elif amps > 18 and amps <= 24:
        calcularSeccionUnipolar(5)
    elif amps > 24 and amps <= 31:
        calcularSeccionUnipolar(6)
    elif amps > 31 and amps <= 42:
        calcularSeccionUnipolar(7)
    elif amps > 42 and amps <= 56:
        calcularSeccionUnipolar(8)
    elif amps > 56 and amps <= 73:
        calcularSeccionUnipolar(9)
    elif amps > 73 and amps <= 89:
        calcularSeccionUnipolar(10)
    elif amps > 89 and amps <= 108:
        calcularSeccionUnipolar(11)
    elif amps > 108 and amps <= 136:
        calcularSeccionUnipolar(12)
    elif amps > 136 and amps <= 164:
        calcularSeccionUnipolar(13)
    elif amps > 164 and amps <= 188:
        calcularSeccionUnipolar(14)
    elif amps > 188 and amps <= 310:
        calcularSeccionUnipolar(15)
    else:
        print("el dato ingresado está fuera de rango.\n")
