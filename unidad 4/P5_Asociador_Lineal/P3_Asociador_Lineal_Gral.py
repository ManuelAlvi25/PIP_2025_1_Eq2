
#Asociador Lineal

#X = Entradas
#Y = Salidas
#W = Y*XPseudoInversa

import numpy as n

archivo = open("instancia_claseExplicacion.txt")
contenido = archivo.readlines()

X = contenido[3:3+int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]

#Y = contenido[3 + int(contenido[1]):]
#Y = [i.strip().split("\t") for i in Y]  # limpia y separa
#Y = [list(map(int, filter(lambda x: x != '', i))) for i in Y]  # elimina vacíos
Y = contenido[3 + int(contenido[1]):]
Y = [i.strip().split("\t") for i in Y]
Y = [[int(x) for x in fila if x.strip() != ''] for fila in Y]

# Validar que todas las filas tengan la misma longitud:
for idx, fila in enumerate(Y):
    print(f"Fila {idx} tiene {len(fila)} elementos")


#Y = contenido[3+int(contenido[1]):]
#Y = [i.split("\t") for i in Y]
#Y = [list(map(int, i.strip())) for i in Y]
#Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = [fila for fila in Y if len(fila) > 0]  # elimina filas vacías
Y = n.array(Y)
#Y = n.array(Y)

Paso1 = X.dot(X.T)
Paso2 = n.linalg.inv(Paso1)
Xpseudo = X.T.dot(Paso2)

W = Y.dot(Xpseudo)

print("X:")
print(X)

print("Y:")
print(Y)

print("W:")
print(W)


###PRUEBA DE LA FUNCIOANLIDA DEL ASOCIADOR LINEA
#VAMOS A PROBAR CADA UNO DE LOS CASOS PARA OBSERVAR SI LA RED ES CAPAZ DE
#CLASIFICAR CORRECTAMENTE

print("Prueba...")

casosCorrectos = 0

#SE DECIDE PREVIAMENTE: ....
# 1 0 0  - BUENO
# 0 1 0  - REGULAR
# 0 0 1  - MALO

#CLASE SALIDA1  SALIDA 2  SALIDA 3
Clases = ["Buena", "Regular", "Malo"]


for i in range(X.shape[1]): #para cada uno de los casos/registros de prueba
    print("Prueba del Caso ", i + 1)
    casoi = X[:,i]
    print("Caso Analizado: ")
    print(casoi)

    Ycasoi = W.dot(casoi)
    print("Salidas Generadas: ")
    print(Ycasoi)

    print("Salidas Real: ")
    Yrealcasoi = Y[:,i]
    print(Yrealcasoi)

    IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
    IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

    if IndexMaxYcasoi == IndexMaxYrealcasoi:
        casosCorrectos +=1

    print("Clase Asignada: ", Clases[IndexMaxYcasoi])
    print("Clase Real: ", Clases[IndexMaxYrealcasoi])
    print()

print("Total de Casos Analizados: ", X.shape[1])
print("Total de Casos Correctos: ", casosCorrectos)

print("Eficiencia del Asociador Lineal: ", casosCorrectos/X.shape[1]*100.0)


#UTILIZACIÓN DEL ASOCIADOR LINEAL...
print("\n\nPrueba de funcionamiento del asociador lineal: ")

#1 0 0  = BUENO
x = [110, 8, 150, 3]  # Primeros 4 valores de la columna 1 (Película_1)
y = "BUENO"

x = n.array(x)
Ycasox = W.dot(x)

print(Ycasox)
IndexMaxYcasoi = list(Ycasox).index(max(Ycasox))

print("Clase Asignada: ", Clases[IndexMaxYcasoi])

print("Correcto " if Clases[IndexMaxYcasoi] == y else "Incorrecto")
