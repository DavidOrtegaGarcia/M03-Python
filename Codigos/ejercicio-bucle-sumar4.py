#coding: utf8
#David Ortega Garcia
#19/03/2018

# Inicializaciones
salir = "N"
numero=1
limite=4
resultado=0

while ( salir=="N" ):
    # Hago cosas
    if (numero%2==0):
        print (numero,end='')
        resultado=resultado+numero
        if (resultado<limite):
            print ('+',end='')
    # Incremento
    numero=numero+1
    # Activo indicador de salida si toca
    if ( numero>limite ): # Condición de salida
        salir = "S"
print ('=',resultado)