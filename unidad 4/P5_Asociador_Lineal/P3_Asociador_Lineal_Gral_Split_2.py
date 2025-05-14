
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



# Paso extra: división en entrenamiento y validación
porcentaje_validacion = int(input("Ingrese el % de validación (ej. 20): "))
#Esta línea pide al usuario que escriba cuánto del total de datos quiere reservar para validación. Por ejemplo,
# si pones 20, el 20% de los datos serán para validar el modelo y el 80% se usarán para entrenarlo.
total_casos = X.shape[1]
num_validacion = int(total_casos * porcentaje_validacion / 100)
num_entrenamiento = total_casos - num_validacion
#X.shape[1] es cuántos casos totales tienes.
#Se calcula el número de casos para validación (num_validacion) con una simple regla de tres.
#Lo que sobra es para entrenamiento (num_entrenamiento).

#Y = n.array(Y)

# Mezclar índices
indices = list(range(total_casos))
import random
random.shuffle(indices)
#Esto crea una lista con los índices de las columnas de X (cada caso) y los revuelve.
# Así no se entrena siempre con los mismos casos ni se valida con los mismos.

# Separar índices
indices_entrenamiento = indices[:num_entrenamiento]
indices_validacion = indices[num_entrenamiento:]
#Parte los índices revueltos: los primeros son para entrenamiento y los últimos para validación.

# Subconjuntos de entrenamiento
X_train = X[:, indices_entrenamiento]
Y_train = Y[:, indices_entrenamiento]

# Subconjuntos de validación
X_val = X[:, indices_validacion]
Y_val = Y[:, indices_validacion]
#Se seleccionan columnas de X y Y según los índices que separaste.
#X_train y Y_train son los que se usan para entrenar la red.
#X_val y Y_val son los que se usan para probar si la red aprendió bien.

Paso1 = X_train.dot(X_train.T)
Paso2 = n.linalg.inv(Paso1)
Xpseudo = X_train.T.dot(Paso2)
W = Y_train.dot(Xpseudo)
#Aquí se hace el cálculo de la matriz de pesos W, solo con los datos de entrenamiento.

#
#Paso1 = X.dot(X.T)
#Paso2 = n.linalg.inv(Paso1)
#Xpseudo = X.T.dot(Paso2)
#W = Y.dot(Xpseudo)
#


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


#for i in range(X.shape[1]): #para cada uno de los casos/registros de prueba
for i in range(X_val.shape[1]):  # solo en los casos de validación #
#Se usa X_val y Y_val para probar el rendimiento de la red con datos que no vio durante
# el entrenamiento, lo que da una medida más justa de si realmente aprendió o memorizó.
    print("Prueba del Caso ", i + 1)
    casoi = X_val[:,i]
    print("Caso Analizado: ")
    print(casoi)

    Ycasoi = W.dot(casoi)
    print("Salidas Generadas: ")
    print(Ycasoi)

    print("Salidas Real: ")
    Yrealcasoi = Y_val[:,i]
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

#2
print(" ")
print(f"Total de casos: {total_casos}")
print(f"Casos de entrenamiento: {num_entrenamiento}")
print(f"Casos de validación: {num_validacion}")

