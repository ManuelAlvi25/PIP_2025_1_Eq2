import sys
from PyQt5 import QtWidgets

import Plantilla_Grafica as interfaz
import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_graficar.clicked.connect(self.graficar)
        self.btn_graficar_2.clicked.connect(self.titulo)
        self.btn_off.clicked.connect(self.grilla)
        self.btn_limpiar.clicked.connect(self.limpiar)

        #                              text      data
        self.sp_estilo.addItem("Estilo: :", ":")
        self.sp_estilo.addItem("Estilo: -", "-")
        self.sp_estilo.addItem("Estilo: --", "--")
        self.sp_estilo.addItem("Estilo: -.", "-.")
        self.sp_estilo.currentIndexChanged.connect(self.estiloLinea)

        self.sp_color.addItem("Negro", "black")
        self.sp_color.addItem("Rojo", "red")
        self.sp_color.addItem("Azul", "blue")
        self.sp_color.addItem("Verde", "green")
        self.sp_color.currentIndexChanged.connect(self.colorLinea)

        self.sp_ancho.setValue(1)
        self.sp_ancho.setMaximum(10)
        self.sp_ancho.setMinimum(1)
        self.sp_ancho.setSingleStep(1)
        self.sp_ancho.valueChanged.connect(self.anchoLinea)

        #VALORES POR DEFECTO:
        self.estiloLinea = ":"
        self.colorLinea = "black"
        self.anchoLinea = 1

        ################################################################################

        self.sp_xmin.setValue(0)
        self.sp_xmin.setMaximum(10000)
        self.sp_xmin.setMinimum(-10000)
        self.sp_xmin.setSingleStep(1)
        self.sp_xmin.valueChanged.connect(self.minX)

        self.sp_xmax.setValue(10)
        self.sp_xmax.setMaximum(10000)
        self.sp_xmax.setMinimum(-10000)
        self.sp_xmax.setSingleStep(1)
        self.sp_xmax.valueChanged.connect(self.maxX)

        self.sp_divisionesX.setValue(10)
        self.sp_divisionesX.setMaximum(10)
        self.sp_divisionesX.setMinimum(1)
        self.sp_divisionesX.setSingleStep(1)
        self.sp_divisionesX.valueChanged.connect(self.divisionesX)

        self.sp_ymin.setValue(0)
        self.sp_ymin.setMaximum(10000)
        self.sp_ymin.setMinimum(-10000)
        self.sp_ymin.setSingleStep(1)
        self.sp_ymin.valueChanged.connect(self.minY)

        self.sp_ymax.setValue(10)
        self.sp_ymax.setMaximum(10000)
        self.sp_ymax.setMinimum(-10000)
        self.sp_ymax.setSingleStep(1)
        self.sp_ymax.valueChanged.connect(self.maxY)

        self.sp_divisionesY.setValue(10)
        self.sp_divisionesY.setMaximum(10)
        self.sp_divisionesY.setMinimum(1)
        self.sp_divisionesY.setSingleStep(1)
        self.sp_divisionesY.valueChanged.connect(self.divisionesY)

        #valores por defecto
        self.xMax = 10
        self.xMin = 1
        self.xDivisiones = 10
        self.yMax = 10
        self.yMin = 1
        self.yDivisiones = 10

        ##
        self.btn_off.setText("ON")

    # Área de los Slots
    def minX(self):
        self.xMin = self.sp_Xmin.value() #obtiene el nuevo valor para el argumento
        self.limpiar() #borra grafica anterior
        self.graficar() #genera la nueva grafica
    def maxX(self):
        self.xMax = self.sp_Xmax.value()
        self.limpiar()
        self.graficar()
    def divisionesX(self):
        self.xDivisiones = self.sp_divisionesX.value()
        self.limpiar()
        self.graficar()
    def minY(self):
        self.yMin = self.sp_Ymin.value()
        self.limpiar()
        self.graficar()
    def maxY(self):
        self.yMax = self.sp_Ymax.value()
        self.limpiar()
        self.graficar()
    def divisionesY(self):
        self.yDivisiones = self.sp_divisionesY.value()
        self.limpiar()
        self.graficar()


    def estiloLinea(self):
        estilo = self.cb_estiloLinea.currentData()
        self.estiloLinea =  estilo

        self.limpiar()
        self.graficar()

    def colorLinea(self):
        color = self.cb_ColorLinea.currentData()
        self.colorLinea = color

        self.limpiar()
        self.graficar()


    def anchoLinea(self):
        ancho = self.sp_anchoLinea.value()
        self.anchoLinea = ancho

        self.limpiar()
        self.graficar()


    def limpiar(self):
        plt.cla()    #borra_todo
        self.canvas.draw()  #vuelve a dibujar

    def titulo(self):
        t = self.txt_titulo.text()
        self.ax.set_title(t)  #establece el titulo

        self.canvas.draw()    # aplica los cambios

    def grilla(self):
        texto = self.btn_grilla.text()
        if texto == "OFF":
            self.btn_grilla.setText("ON")
            plt.grid(False)
        else: #ON
            self.btn_grilla.setText("OFF")
            plt.grid(True)

        self.canvas.draw()

    def graficar(self):
        polinomio = self.txt_polinomio.text()  # Ej: 2x^2+3x+4
        polinomio = polinomio.replace("^","**")  # 2x**2+3x+4

        #tabular...  valores de X con base en los cuales pueda obtener los valores de y
        X = [i for i in range(self.xMin, self.xMax+1)] #lista de comprension
        print("Valores de X: ")
        print(X)

        #y = polinomio.replace("x","*("+str(x[0])+")")
        y = [eval(polinomio.replace("x","*("+str(x)+")")) for x in X]
        print("Valores de Y: ")
        print(y)

        self.ax.plot(X, y,
                 linestyle= self.estiloLinea,  #: - -- -.
                 color= self.colorLinea,  # color de la linea
                 linewidth= self.anchoLinea,  # tamaño de la linea
                 marker=".",  # o . *  x   1
                 markersize=4,
                 markerfacecolor="yellow",  # color interno del marcador
                 markeredgewidth=1,  # tamaño del borde del marcador
                 markeredgecolor="blue",  # color del borde del marcador
                 dash_capstyle="butt",  # dash or solid : "butt" "round" "projecting"
                 dash_joinstyle="miter"  # dash or solid : "miter" "round" "bevel"
                 )

        #Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax+1)
        self.ax.set_ylim(self.yMin, self.yMax + 1)

        self.ax.set_xlabel("Eje X")
        self.ax.set_ylabel("Eje Y")

        #totalelementosenX/totaldivisionesDeseadas = 8
        #mediante un ciclo se obtiene:

        #si comienzo con xmin en 0 seria:
        #xtick = [0, 10, 20, 30, 40, 50, 60, 70, 80]

        #si comienzo con xmin en n seria:
        xtick = []
        for i in range(-30, 30+1, 10):
            xtick.append(i)
        print("Ticks para X: ")
        print(xtick)


        xtick = [2, 5, 15, 25, 35, 45, 55, 65, 75, 85]


        self.ax.set_xticks(xtick)


        self.ax.set_yticks(y)   #NOTA.. CHECK!

        #una posibilidad para establecer los ticks sería:
        #Tomar el conjunto y dividirlo entre el total de "divisiones" que el usuario desee


        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
