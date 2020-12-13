#electapp v0.1
#calculo de secciones de cable en extraido de la tabla de argenplas
#************Listas*************
seccion=[0.50,0.75,1.0,1.50,2.50,4.0,6.0,10.0,16.0,25.0,35.0,50.0,70.0,95.0,120.0,150.0,185.0]
diaExterior=[2.15,2.3,2.7,3.0,3.65,4.3,4.8,6.3,7.7,9.9,11.1,12.9,15.55,17.2,19.1,21.8]
peso=[0.89,1.14,1.57,2.09,3.32,5.0,6.80,11.9,17.9,29.0,39.0,55.4,76.4,98.13,124.9,163.5]
corrienteMax=[3.0,8.0,11.0,13.0,18.0,24.0,31.0,42.0,56.0,73.0,89.0,108.0,136.0,164.0,188.0,310.0]
fusible=[2.0,6.0,10.0,10.0,16.0,20.0,25.0,50.0,63.0,80.0,100.0,125.0,160.0,160.0,250.0]

#caculo de corriente (amperios)

watts =float(input('ingrese la carga en watts\n'))
#volts =float(input('ingrese el voltaje\n'))
volts = 220.0
amps = watts/volts
if amps<=3:#1
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[0]:.2f}"),' mm2')
    print('el diametro exterior del cable es de:\t\t'+ str(f"{diaExterior[0]:.2f}"),' mm')
    print('el peso por cada 100mts es de:\t\t\t'+ str(f"{peso[0]:.2f}"),' kg')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMax[0]:.2f}"),' Amp')
    print('fusible NH es de:\t\t\t\t'+ str(f"{fusible[0]:.2f}"),' Amp')
elif amps>3 and amps<=8:#2
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[1]:.2f}"),' mm2')
    print('el diametro exterior del cable es de:\t\t'+ str(f"{diaExterior[1]:.2f}"),' mm')
    print('el peso por cada 100mts es de:\t\t\t'+ str(f"{peso[1]:.2f}"),' kg')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMax[1]:.2f}"),' Amp')
    print('fusible NH es de:\t\t\t\t'+ str(f"{fusible[1]:.2f}"),' Amp')
elif amps>8 and amps<=11:#3
    print('la seccion nominal es de:\t\t\t'+ str(f"{seccion[2]:.2f}"),' mm2')
    print('el diametro exterior del cable es de:\t\t'+ str(f"{diaExterior[2]:.2f}"),' mm')
    print('el peso por cada 100mts es de:\t\t\t'+ str(f"{peso[2]:.2f}"),' kg')
    print('la corriente admisible en amperios es de:\t'+ str(f"{corrienteMax[2]:.2f}"),' Amp')
    print('fusible NH es de:\t\t\t\t'+ str(f"{fusible[2]:.2f}"),' Amp')
elif amps>11 and amps<=13:#4
    print('la seccion nominal es de: '+ str(f"{seccion[3]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[3]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[3]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[3]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[3]:.2f}"),' Amp')
elif amps>13 and amps<=18:#5
    print('la seccion nominal es de: '+ str(f"{seccion[4]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[4]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[4]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[4]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[4]:.2f}"),' Amp')
elif amps>18 and amps<=24:#6
    print('la seccion nominal es de: '+ str(f"{seccion[5]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[5]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[5]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[5]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[5]:.2f}"),' Amp')
elif amps>24 and amps<=31:#7
    print('la seccion nominal es de: '+ str(f"{seccion[6]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[6]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[6]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[6]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[6]:.2f}"),' Amp')
elif amps>31 and amps<=42:#8
    print('la seccion nominal es de: '+ str(f"{seccion[7]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[7]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[7]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[7]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[7]:.2f}"),' Amp')
elif amps>42 and amps<=56:#9
    print('la seccion nominal es de: '+ str(f"{seccion[8]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[8]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[8]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[8]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[8]:.2f}"),' Amp')
elif amps>56 and amps<=11:#10
    print('la seccion nominal es de: '+ str(f"{seccion[9]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[9]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[9]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[9]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[9]:.2f}"),' Amp')
elif amps>8 and amps<=73:#11
    print('la seccion nominal es de: '+ str(f"{seccion[10]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[10]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[10]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[10]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[10]:.2f}"),' Amp')
elif amps>73 and amps<=89:#12
    print('la seccion nominal es de: '+ str(f"{seccion[11]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[11]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[11]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[11]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[11]:.2f}"),' Amp')
elif amps>89 and amps<=108:#13
    print('la seccion nominal es de: '+ str(f"{seccion[12]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[12]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[1]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[12]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[12]:.2f}"),' Amp')
elif amps>108 and amps<=136:#14
    print('la seccion nominal es de: '+ str(f"{seccion[13]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[13]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[13]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[13]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[13]:.2f}"),' Amp')
elif amps>136 and amps<=164:#15
    print('la seccion nominal es de: '+ str(f"{seccion[14]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[14]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[14]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[2]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[14]:.2f}"),' Amp')
elif amps>164 and amps<=188:#16
    print('la seccion nominal es de: '+ str(f"{seccion[15]:.2f}"),' mm2')
    print('el diametro exterior del cable es de: '+ str(f"{diaExterior[15]:.2f}"),' mm')
    print('el peso por cada 100mts es de: '+ str(f"{peso[15]:.2f}"),' kg')
    print('la corriente admisible en amperios es de: '+ str(f"{corrienteMax[15]:.2f}"),' Amp')
    print('fusible NH es de: '+ str(f"{fusible[15]:.2f}"),' Amp')
else:
    print('el dato ingresado está fuera de rango.\n')
salir = input('desea volver a calcular: s,n')

if salir == s:
    print('gracias por usar electapp')
    break
else:
    print('termino')
