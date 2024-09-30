# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton #type: ignore

app = QApplication(sys.argv)

botao = QPushButton('Texto do botao')
botao.setStyleSheet('font-size: 40px; color: blue;') # Colocando estilos (css)
botao.show() # Adiciona o widget na hierarquia e exibe a janela

app.exec() #Inicia o loop da aplicação