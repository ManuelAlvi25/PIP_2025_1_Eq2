import numpy as np

# Abrimos el archivo y leemos el contenido
archivo = open("instancia_claseExplicacion.txt")
contenido = archivo.readlines()
archivo.close()

# Primero obtenemos el número de entradas (X) y salidas (Y) desde las líneas correspondientes
num_entradas = int(contenido[0].strip())  # Número de entradas (primera línea)
num_salidas = int(contenido[1].strip())   # Número de salidas (segunda línea)

# Procesamos las entradas X
X = contenido[2:2 + num_entradas]  # Cortamos las líneas de entradas
X = [i.strip().split("\t") for i in X]  # Eliminamos saltos de línea con strip() y dividimos por tabuladores
X = [list(map(int, i)) for i in X]  # Convertimos los elementos a enteros

# Procesamos las salidas Y
Y = contenido[2 + num_entradas:]  # Cortamos las líneas de salidas
Y = [i.strip().split("\t") for i in Y]  # Lo mismo para las salidas
Y = [list(map(int, i)) for i in Y]  # Convertimos a enteros

# Convertimos X y Y en arrays de numpy para poder realizar operaciones matemáticas
X = np.array(X)
Y = np.array(Y)

# Cálculos del asociador lineal
Paso1 = X.dot(X.T)
Paso2 = np.linalg.inv(Paso1)
Xpseudo = X.T.dot(Paso2)

W = Y.dot(Xpseudo)

print("X:")
print(X)

print("Y:")
print(Y)

print("W:")
print(W)

### PRUEBA DE FUNCIONALIDAD DEL ASOCIADOR LINEAL
print("Prueba...")

casosCorrectos = 0

# CLASE SALIDA1  SALIDA 2  SALIDA 3
Clases = ["Buena", "Regular", "Malo"]

for i in range(X.shape[1]):  # Para cada uno de los casos/registros de prueba
    print("Prueba del Caso ", i + 1)
    casoi = X[:, i]
    print("Caso Analizado: ")
    print(casoi)

    Ycasoi = W.dot(casoi)
    print("Salidas Generadas: ")
    print(Ycasoi)

    print("Salidas Real: ")
    Yrealcasoi = Y[:, i]
    print(Yrealcasoi)

    IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
    IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

    if IndexMaxYcasoi == IndexMaxYrealcasoi:
        casosCorrectos += 1

    print("Clase Asignada: ", Clases[IndexMaxYcasoi])
    print("Clase Real: ", Clases[IndexMaxYrealcasoi])
    print()

print("Total de Casos Analizados: ", X.shape[1])
print("Total de Casos Correctos: ", casosCorrectos)

print("Eficiencia del Asociador Lineal: ", casosCorrectos / X.shape[1] * 100.0)

# UTILIZACIÓN DEL ASOCIADOR LINEAL...
print("\n\nPrueba de funcionamiento del asociador lineal: ")

# Ejemplo de entrada a clasificar
x = [78, 53, 11, 30, 86, 23]
y = "BUENO"

x = np.array(x)
Ycasox = W.dot(x)

print(Ycasox)
IndexMaxYcasoi = list(Ycasox).index(max(Ycasox))

print("Clase Asignada: ", Clases[IndexMaxYcasoi])

print("Correcto " if Clases[IndexMaxYcasoi] == y else "Incorrecto")
