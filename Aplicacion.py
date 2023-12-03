import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QPushButton, QLabel, QStackedWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("diseñointerfaz.ui", self)
        
        self.Submenu.hide()
        self.Ingreso_datos.hide()
        
        self.Maximo.clicked.connect(self.pantalla_maximizar)
        self.Minimo.clicked.connect(self.pantalla_minimizar)
        self.Minimizar.clicked.connect(self.minimizar_app)
        self.Cerrar.clicked.connect(self.cerrar_app)
        self.Salir.clicked.connect(self.salir_app)
        self.RegistroClientes.clicked.connect(self.mostrar_submenu_clientes)
        self.RegistroAntibioticos.clicked.connect(self.mostrar_submenu_antibioticos)
        self.RegistroPesticidas.clicked.connect(self.mostrar_submenu_pesticidas)
        self.RegistroFertilizantes.clicked.connect(self.mostrar_submenu_fertilizantes)
        self.Facturacion.clicked.connect(self.mostrar_submenu_factura)
        self.pushButton_5.clicked.connect(self.crear_antibiotico)
        self.pushButton_6.clicked.connect(self.listar_antibiotico)
        self.pushButton_7.clicked.connect(self.eliminar_antibiotico)
        self.pushButton_8.clicked.connect(self.cerrar_submenu)
        self.pushButton.clicked.connect(self.crear_cliente)
        self.pushButton_2.clicked.connect(self.listar_cliente)
        self.pushButton_3.clicked.connect(self.eliminar_cliente)
        self.pushButton_4.clicked.connect(self.cerrar_submenu)
        self.pushButton_17.clicked.connect(self.crear_factura)
        self.pushButton_19.clicked.connect(self.listar_factura)
        self.pushButton_21.clicked.connect(self.cerrar_submenu)
        self.pushButton_9.clicked.connect(self.crear_fertilizante)
        self.pushButton_10.clicked.connect(self.listar_fertilizante)
        self.pushButton_11.clicked.connect(self.eliminar_fertilizante)
        self.pushButton_12.clicked.connect(self.cerrar_submenu)
        self.pushButton_13.clicked.connect(self.crear_pesticida)
        self.pushButton_14.clicked.connect(self.listar_pesticida)
        self.pushButton_15.clicked.connect(self.eliminar_pesticida)
        self.pushButton_16.clicked.connect(self.cerrar_submenu)
        self.pushButton_18.clicked.connect(self.verificar_creacion_cliente)
        self.pushButton_23.clicked.connect(self.verificar_creacion_antibiotico)
        self.pushButton_22.clicked.connect(self.verificar_creacion_fertilizante)
        self.pushButton_24.clicked.connect(self.verificar_creacion_pesticida)
        self.pushButton_25.clicked.connect(self.verificar_eliminacion_antibiotico)
        self.pushButton_26.clicked.connect(self.verificar_eliminacion_cliente)
        self.pushButton_27.clicked.connect(self.verificar_eliminacion_fertilizante)
        self.pushButton_28.clicked.connect(self.verificar_eliminacion_pesticida)
        
    def pantalla_maximizar (self) :
        self.showMaximized()
        
    def pantalla_minimizar (self) :
        self.showNormal()
        
    def minimizar_app (self) :
        self.showMinimized()
        
    
    def cerrar_app(self):
        QApplication.quit()
        #poner efecto hoover en qtdesigner
        
    def salir_app(self):
        QApplication.quit()
 

    def mostrar_submenu_clientes (self) :
        self.Submenu.show()
        self.stackedWidget1.setCurrentIndex(0)
        
    
        
    def mostrar_submenu_antibioticos (self) :
        self.Submenu.show()
        self.stackedWidget1.setCurrentIndex(4)
        
    
    def mostrar_submenu_pesticidas (self) :
        self.Submenu.show()
        self.stackedWidget1.setCurrentIndex(1)
        
    def mostrar_submenu_fertilizantes (self) :
        self.Submenu.show()
        self.stackedWidget1.setCurrentIndex(2)
        
        
    def mostrar_submenu_factura (self) :
        self.Submenu.show()
        self.stackedWidget1.setCurrentIndex(3)

    def cerrar_submenu (self) :
        self.Submenu.hide()
        self.Ingreso_datos.hide()

    def crear_cliente (self) :
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(11)   
    
    def crear_antibiotico (self) : 
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(6)
        
    def crear_factura (self):
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(9)
        
    def crear_fertilizante (self):
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(0)
        
    def crear_pesticida (self):
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(3)
    
    def listar_pesticida (self):
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(4)
    
    def listar_antibiotico (self):
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(2)
    
    def listar_fertilizante (self) :
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(12)
        
        
    def listar_cliente (self) :
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(7)
        
    def listar_factura (self) :
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(10)
        
    def eliminar_cliente (self) :
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(13)
       
        
    def eliminar_antibiotico (self):
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(1)
    
    def eliminar_pesticida (self):
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(5)
    
    def eliminar_fertilizante (self):
        self.Ingreso_datos.show()
        self.stackedWidget_2.setCurrentIndex(8)
    

    
    def verificar_creacion_cliente(self):
        nombre_cliente = self.lineEdit.text()
        cedula_cliente = self.lineEdit_2.text()

        
        if not nombre_cliente or not cedula_cliente:
           
            QMessageBox.warning(self, 'Advertencia', 'Por favor, complete ambos campos antes de confirmar.')
        else:
           
            mensaje = f'nombre: {nombre_cliente}\ncedula: {cedula_cliente}'
            QMessageBox.information(self, 'Información', mensaje)
    
    
    def verificar_creacion_antibiotico (self):
        nombre_antibiotico = self.lineEdit_10.text()
        dosis_antibiotico = self.lineEdit_11.text()
        precio_antibiotico = self.lineEdit_8.text()
        
        if not nombre_antibiotico or not dosis_antibiotico or not precio_antibiotico :
           
            QMessageBox.warning(self, 'Advertencia', 'Por favor, complete los campos antes de confirmar.')
        else:
           
            mensaje = f'nombre antibiotico: {nombre_antibiotico}\ndosis: {dosis_antibiotico}\nprecio: {precio_antibiotico}'
            QMessageBox.information(self, 'Información', mensaje)
            
            
            
    
    def verificar_creacion_fertilizante (self):
        registro_ica_fertilizante = self.lineEdit_3.text()
        nombre_fertilizante = self.lineEdit_5.text()
        frecuencia_aplicacion_fertilizante = self.lineEdit_4.text()
        precio_fertilizante = self.lineEdit_6.text()
        ultima_fecha_aplicacion_fertilizante = self.lineEdit_7.text()
        
        
        if not registro_ica_fertilizante or not nombre_fertilizante or not frecuencia_aplicacion_fertilizante or not precio_fertilizante or not ultima_fecha_aplicacion_fertilizante :
           
            QMessageBox.warning(self, 'Advertencia', 'Por favor, complete los campos antes de confirmar.')
        else:
           
            mensaje = f'registro ica: {registro_ica_fertilizante}\nnombre: {nombre_fertilizante}\nfrecuencia aplicacion: {frecuencia_aplicacion_fertilizante}\nprecio: {precio_fertilizante}\nultima aplicacion: {ultima_fecha_aplicacion_fertilizante}'
            QMessageBox.information(self, 'Información', mensaje)
        
        
        
    def verificar_creacion_pesticida (self) :
        registro_ica_pesticida = self.lineEdit_9.text()
        nombre_pesticida = self.lineEdit_13.text()
        frecuencia_aplicacion_pesticida = self.lineEdit_12.text()
        precio_pesticida = self.lineEdit_17.text()
        ultima_fecha_aplicacion_pesticida = self.lineEdit_18.text()
        
        
        if not registro_ica_pesticida or not nombre_pesticida or not frecuencia_aplicacion_pesticida or not precio_pesticida or not ultima_fecha_aplicacion_pesticida :
           
            QMessageBox.warning(self, 'Advertencia', 'Por favor, complete los campos antes de confirmar.')
        else:
           
            mensaje = f'registro ica: {registro_ica_pesticida}\nnombre: {nombre_pesticida}\nfrecuencia aplicacion: {frecuencia_aplicacion_pesticida}\nprecio: {precio_pesticida }\nultima aplicacion: {ultima_fecha_aplicacion_pesticida}'
            QMessageBox.information(self, 'Información', mensaje)
        
        
    def verificar_eliminacion_antibiotico (self) :
        nombre_antibiotico_eliminar = self.lineEdit_19.text()
        
        
        if not nombre_antibiotico_eliminar :
           
            QMessageBox.warning(self, 'Advertencia', 'Por favor, complete el campo antes de confirmar.')
        else:
           
            mensaje = f'Antibiotico eliminado'
            QMessageBox.information(self, 'Información', mensaje)
        
        
    def verificar_eliminacion_cliente (self) :
        cedula_cliente_eliminar = self.lineEdit_23.text()
        
        if not cedula_cliente_eliminar :
            
             QMessageBox.warning(self, 'Advertencia', 'Por favor, complete el campo antes de confirmar.')
        else:
           
            mensaje = f'cliente eliminado'
            QMessageBox.information(self, 'Información', mensaje)
        
    
    def verificar_eliminacion_fertilizante (self) :
        nombre_fertilizante_eliminar = self.lineEdit_24.text()
        
        if not nombre_fertilizante_eliminar :
            
             QMessageBox.warning(self, 'Advertencia', 'Por favor, complete el campo antes de confirmar.')
        else:
           
            mensaje = f'fertilizante eliminado'
            QMessageBox.information(self, 'Información', mensaje) 
        
    def verificar_eliminacion_pesticida (self) :
        nombre_pesticida_eliminar = self.lineEdit_25.text()
            
        if not nombre_pesticida_eliminar :
            
             QMessageBox.warning(self, 'Advertencia', 'Por favor, complete el campo antes de confirmar.')
        else:
           
            mensaje = f'pesticida eliminado'
            QMessageBox.information(self, 'Información', mensaje)     
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())

        