import sys
import os
import statistics
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Proyecto unidad 1.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.datos = []

    def cargar(self):
        if not os.path.exists("Archivos/Datos y Resultados.csv"):
            self.msj("El archivo no existe.")
            return

        try:
            with open("Archivos/Datos y Resultados.csv", "r") as archivo:
                contenido = archivo.readlines()

                # Encontrar la sección "Resultados:"
                indice_resultados = -1
                for i, linea in enumerate(contenido):
                    if "Resultados:" in linea:
                        indice_resultados = i
                        break

                if indice_resultados == -1:
                    self.msj("No se encontraron los resultados en el archivo.")
                    return

                # Los datos están antes de "Resultados:"
                datos_lineas = contenido[:indice_resultados]
                self.datos = []

                for linea in datos_lineas:
                    try:
                        # Solo agregar números válidos (saltarse líneas vacías o no numéricas)
                        if linea.strip():  # Asegurarse de que la línea no esté vacía
                            self.datos.append(float(linea.strip()))
                    except ValueError:
                        continue  # Ignorar las líneas que no son números

            self.mostrar_datos()
            self.calcular_estadisticas()
            self.msj("Datos cargados con éxito!")

        except Exception as e:
            self.msj(f"Error al cargar los datos: {str(e)}")  # Captura de errores al leer el archivo

    def agregar(self):
        try:
            # Verificar si el objeto txt_valores existe
            if not hasattr(self, 'txt_valores'):
                raise AttributeError("No se encontró 'txt_valores'. Verifica el nombre en Qt Designer.")

            texto = self.txt_valores.toPlainText().strip()  # Obtener texto y limpiar espacios
            if not texto:  # Verificar si el usuario no ingresó nada
                self.msj("Debe ingresar al menos un número.")
                return

            valores = texto.split(",")  # Separar los valores por comas
            valores_limpios = []

            for x in valores:
                x = x.strip()
                try:
                    valores_limpios.append(float(x))  # Convertir a número
                except ValueError:
                    self.msj(f"'{x}' no es un número válido.")
                    return  # Si hay un error, no agregamos nada

            if not valores_limpios:
                self.msj("Ingrese números válidos separados por comas.")
                return

            self.datos.extend(valores_limpios)  # Agregar los valores a la lista
            self.mostrar_datos()
            self.calcular_estadisticas()

            self.txt_valores.clear()  # Limpiar el campo después de agregar los números
        except AttributeError as e:
            self.msj(f"Error: {str(e)}. Verifica los nombres en Qt Designer.")
        except Exception as e:
            self.msj(f"Error inesperado: {str(e)}")  # Captura errores desconocidos

    def calcular_estadisticas(self):
        if not self.datos:
            return

        self.txt_menor.setText(str(min(self.datos)))
        self.txt_mayor.setText(str(max(self.datos)))
        self.txt_media.setText(str(statistics.mean(self.datos)))
        self.txt_mediana.setText(str(statistics.median(self.datos)))
        self.txt_moda.setText(str(statistics.mode(self.datos)))
        self.txt_desviacion.setText(str(statistics.stdev(self.datos) if len(self.datos) > 1 else 0))
        self.txt_varianza.setText(str(statistics.variance(self.datos) if len(self.datos) > 1 else 0))

    def mostrar_datos(self):
        self.txt_lista.setPlainText(", ".join(map(str, self.datos)))

    def guardar(self):
        try:
            # Verificar si la carpeta 'Archivos' existe
            if not os.path.exists("Archivos"):
                os.makedirs("Archivos")  # Crear la carpeta si no existe

            # Abrir el archivo "Datos y Resultados.csv" para escritura
            with open("Archivos/Datos y Resultados.csv", "w") as archivo:
                # Guardar los datos
                archivo.write("Datos:\n")
                for dato in self.datos:
                    archivo.write(str(dato) + "\n")

                # Guardar los resultados
                archivo.write("\nResultados:\n")
                archivo.write(f"Menor,{min(self.datos)}\n")
                archivo.write(f"Mayor,{max(self.datos)}\n")
                archivo.write(f"Media,{statistics.mean(self.datos)}\n")
                archivo.write(f"Mediana,{statistics.median(self.datos)}\n")
                archivo.write(f"Moda,{statistics.mode(self.datos)}\n")
                archivo.write(f"Desviacion,{statistics.stdev(self.datos) if len(self.datos) > 1 else 0}\n")
                archivo.write(f"Varianza,{statistics.variance(self.datos) if len(self.datos) > 1 else 0}\n")

            self.msj("Datos y resultados guardados con éxito!")  # Mensaje de éxito
        except Exception as e:
            self.msj(f"Error al guardar los archivos: {str(e)}")  # Mensaje de error

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
