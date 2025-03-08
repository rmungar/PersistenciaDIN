import os
from Config.paths import basedir
from PyQt6.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QDialogButtonBox, QDialog


class FormularioEmergente(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Añadir un comentario")
        self.setGeometry(100, 100, 300, 200)

        # Layout principal
        layout = QVBoxLayout()
        self.comentario_input = QLineEdit(self)
        self.comentario_input.setPlaceholderText("Comentario")
        layout.addWidget(QLabel("Comentar"))
        layout.addWidget(self.comentario_input)

        # Botones de Aceptar y Cancelar
        botones = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, 
            self
        )
        botones.accepted.connect(self.accept)  # Cierra el diálogo y retorna `QDialog.Accepted`
        botones.rejected.connect(self.reject)  # Cierra el diálogo y retorna `QDialog.Rejected`
        layout.addWidget(botones)

        self.setLayout(layout)

    def obtener_datos(self):
        return {
            "Comentario": self.comentario_input.text(),
        }