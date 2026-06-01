import sys
import subprocess
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)


class VentanaRelojeria(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Relojería B - TP Simulación")
        self.resize(450, 300)

        layout = QVBoxLayout()

        # =====================================
        # PARAMETROS
        # =====================================

        layout.addWidget(QLabel("Máximo de iteraciones"))
        self.iteraciones = QLineEdit("100000")
        layout.addWidget(self.iteraciones)

        layout.addWidget(QLabel("Tiempo de simulación"))
        self.tiempo = QLineEdit("1000000")
        layout.addWidget(self.tiempo)

        layout.addWidget(QLabel("Mostrar desde fila"))
        self.desde = QLineEdit("0")
        layout.addWidget(self.desde)

        layout.addWidget(QLabel("Cantidad filas a mostrar"))
        self.cantidad = QLineEdit("300")
        layout.addWidget(self.cantidad)

        # =====================================
        # BOTON EJECUTAR
        # =====================================

        boton_simular = QPushButton("Ejecutar Simulación")
        boton_simular.clicked.connect(self.ejecutar)
        layout.addWidget(boton_simular)

        # =====================================
        # BOTON EXCEL
        # =====================================

        boton_excel = QPushButton("Abrir Excel")
        boton_excel.clicked.connect(self.abrir_excel)
        layout.addWidget(boton_excel)

        self.setLayout(layout)

    # =========================================
    # EJECUTAR SIMULACION
    # =========================================

    def ejecutar(self):

        datos = (
            f"{self.iteraciones.text()}\n"
            f"{self.tiempo.text()}\n"
            f"{self.desde.text()}\n"
            f"{self.cantidad.text()}\n"
        )

        try:

            resultado = subprocess.run(
                [sys.executable, "main.py"],
                input=datos,
                text=True,
                capture_output=True
            )

            if resultado.returncode == 0:

                texto = resultado.stdout

                if "RESULTADOS FINALES" in texto:
                    texto = texto[
                        texto.find("RESULTADOS FINALES"):
                    ]

                QMessageBox.information(
                    self,
                    "Resultados de la Simulación",
                    texto
                )

            else:

                QMessageBox.critical(
                    self,
                    "Error",
                    resultado.stderr
                )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    # =========================================
    # ABRIR EXCEL
    # =========================================

    def abrir_excel(self):

        try:

            subprocess.run(
                ["open", "resultados/simulacion.xlsx"]
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )


# =============================================
# MAIN
# =============================================

app = QApplication(sys.argv)

ventana = VentanaRelojeria()
ventana.show()

sys.exit(app.exec())