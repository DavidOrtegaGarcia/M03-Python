#coding: utf8
#David Ortega Garcia
#19/03/2018

# Inicializaciones
salir = "N"
numero=1
limite=5
resultado=0

while ( salir=="N" ):
	# Hago cosas
    print (numero,end='')
    if (numero<limite):
        print ('+',end=''),
    # Incremento
    resultado=resultado+numero
    numero=numero+1
    # Activo indicador de salida si toca
    if (numero>limite ): # Condición de salida
    	    salir = "S"
print ('=',resultado)
