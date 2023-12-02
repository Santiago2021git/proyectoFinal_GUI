from UI import InterfazGrafica

'''
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QPushButton, QLabel, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("diseñointerfaz.ui",self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())

'''

print("BIENVENIDO A LA TIENDA AGRICOLA S&S")

InterfazGrafica.escoger_opciones()
