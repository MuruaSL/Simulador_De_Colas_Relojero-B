import sys
from tracemalloc import start 
from PyQt6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QWidget, QLabel, 
QLineEdit, QPushButton, QVBoxLayout, QPushButton, QMessageBox,
QCheckBox)

from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setMinimumSize(800, 400)
        self.setWindowTitle("Simulación: Relojeria B")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        '''general'''
        self.main_label = QLabel(self)
        self.main_label.setText("Defina Los parametros de la Simulación:")
        self.main_label.setFont(QFont("Arial", 20))

        '''CLIENTES'''
        self.cliente_label = QLabel(self)
        self.cliente_label.setText("Defina la llegada del cliente (uniforme):")
        self.cliente_label.setFont(QFont("Arial", 20))

        self.llegada_clientes_min_input = QLineEdit(self)
        self.llegada_clientes_min_input.setPlaceholderText("Llegada de Clientes Min")
        self.llegada_clientes_max_input = QLineEdit(self)
        self.llegada_clientes_max_input.setPlaceholderText("Llegada de Clientes Max")

        self.accion_cliente_label = QLabel(self)
        self.accion_cliente_label.setText("Defina la probabilidad de Acción del Cliente "
        "(Comprar / Entregar / Retirar):")
        self.accion_cliente_label.setFont(QFont("Arial", 20))
        self.clientes_comprar = QLineEdit(self)
        self.clientes_comprar.setPlaceholderText("Probabilidad de Comprar")
        self.clientes_entregar = QLineEdit(self)
        self.clientes_entregar.setPlaceholderText("Probabilidad de Entregar")
        self.clientes_retirar = QLineEdit(self)
        self.clientes_retirar.setPlaceholderText("Probabilidad de Retirar")


        '''AYUDANTE'''
        self.ayudante_label = QLabel(self)
        self.ayudante_label.setText("Ayudante:")
        self.ayudante_label.setFont(QFont("Arial", 20))
        self.tiempo_atencion_compra_min = QLineEdit(self)
        self.tiempo_atencion_compra_min.setPlaceholderText("Tiempo de Atención para Compra")
        self.tiempo_atencion_compra_max = QLineEdit(self)
        self.tiempo_atencion_compra_max.setPlaceholderText("Tiempo de Atención para Compra")
        self.tiempo_atencion_entrega = QLineEdit(self)
        self.tiempo_atencion_entrega.setPlaceholderText("Tiempo de Atención para Entrega")
        self.tiempo_atencion_retiro = QLineEdit(self)
        self.tiempo_atencion_retiro.setPlaceholderText("Tiempo de Atención para Retiro")


        '''RELOJERO'''
        self.relojero_label = QLabel(self)
        self.relojero_label.setText("Relojero:")
        self.relojero_label.setFont(QFont("Arial", 20))
        self.tiempo_reparacion_relojero_min = QLineEdit(self)
        self.tiempo_reparacion_relojero_min.setPlaceholderText("Tiempo de Reparación para Relojero")
        self.tiempo_reparacion_relojero_max = QLineEdit(self)
        self.tiempo_reparacion_relojero_max.setPlaceholderText("Tiempo de Reparación para Relojero")
        self.probabilidad_tomar_cafe = QLineEdit(self)
        self.probabilidad_tomar_cafe.setPlaceholderText("Probabilidad de Tomar Café")
        self.tiempo_tomar_cafe = QLineEdit(self)
        self.tiempo_tomar_cafe.setPlaceholderText("Tiempo de Tomar Café")

        '''Boton'''
        self.start_button = QPushButton("Iniciar Simulación", self)
        self.start_button.clicked.connect(self.iniciar_simulacion) #TODO: conectar a la función de iniciar simulación

        self.cantidad_iteraciones = QLineEdit(self)
        self.cantidad_iteraciones.setPlaceholderText("Cantidad de Iteraciones")
        self.tiempo_simulacion = QLineEdit(self)
        self.tiempo_simulacion.setPlaceholderText("Tiempo de Simulación")
        self.generar_layout()

    def generar_layout(self):

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.main_label, 0, 0, 1, 2)
        '''CLIENTES'''
        self.main_grid.addWidget(self.cliente_label, 1, 0, 1, 2)
        h_layout_llegada_clientes = QHBoxLayout()
        h_layout_llegada_clientes.addWidget(self.llegada_clientes_min_input)
        h_layout_llegada_clientes.addWidget(self.llegada_clientes_max_input)
        self.main_grid.addLayout(h_layout_llegada_clientes, 2, 0, 1, 2)

        self.main_grid.addWidget(self.accion_cliente_label, 3, 0, 1, 2)
        h_layout_accion_cliente = QHBoxLayout()
        h_layout_accion_cliente.addWidget(self.clientes_comprar)
        h_layout_accion_cliente.addWidget(self.clientes_entregar)
        h_layout_accion_cliente.addWidget(self.clientes_retirar)
        self.main_grid.addLayout(h_layout_accion_cliente, 4, 0, 1, 2)


        '''AYUDANTE'''
        self.main_grid.addWidget(self.ayudante_label, 5, 0, 1, 2)
        h_layout_ayudante = QHBoxLayout()
        h_layout_ayudante.addWidget(self.tiempo_atencion_compra_min)
        h_layout_ayudante.addWidget(self.tiempo_atencion_compra_max)
        h_layout_ayudante.addWidget(self.tiempo_atencion_entrega)
        h_layout_ayudante.addWidget(self.tiempo_atencion_retiro)
        self.main_grid.addLayout(h_layout_ayudante, 6, 0, 1, 2)
        
        '''RELOJERO'''
        self.main_grid.addWidget(self.relojero_label, 7, 0, 1, 2)
        h_layout_relojero = QHBoxLayout()
        h_layout_relojero.addWidget(self.tiempo_reparacion_relojero_min)
        h_layout_relojero.addWidget(self.tiempo_reparacion_relojero_max)
        h_layout_relojero.addWidget(self.probabilidad_tomar_cafe)
        h_layout_relojero.addWidget(self.tiempo_tomar_cafe)
        self.main_grid.addLayout(h_layout_relojero, 8, 0, 1, 2)

        '''SIMULACION'''
        h_layout_simulacion = QHBoxLayout()
        h_layout_simulacion.addWidget(self.cantidad_iteraciones)
        h_layout_simulacion.addWidget(self.tiempo_simulacion)
        h_layout_simulacion.addWidget(self.start_button)
        self.main_grid.addLayout(h_layout_simulacion, 9, 0, 1, 2)

        self.setLayout(self.main_grid)

    def iniciar_simulacion(self):
        pass
        
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())        
        


