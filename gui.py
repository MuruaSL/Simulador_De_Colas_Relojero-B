
import sys
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)

class VentanaRelojeria(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relojería B - TP Simulación")
        self.resize(400, 250)

        layout = QVBoxLayout()

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

        boton = QPushButton("Ejecutar simulación")
        boton.clicked.connect(self.ejecutar)

        layout.addWidget(boton)

        self.setLayout(layout)

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
            print(resultado.returncode)
            print(resultado.stderr)

            with open("resultado_simulacion.txt", "w", encoding="utf-8") as f:
                f.write("=== STDOUT ===\n")
                f.write(resultado.stdout)

                f.write("\n\n=== STDERR ===\n")
                f.write(resultado.stderr)

            QMessageBox.information(
                self,
                "Finalizado",
                "La simulación terminó.\nSe generó resultado_simulacion.txt"
            )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

app = QApplication(sys.argv)
ventana = VentanaRelojeria()
ventana.show()
sys.exit(app.exec())
