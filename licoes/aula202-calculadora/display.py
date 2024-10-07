from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        # Setando o tamanho da fonte
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        # Setando a Altura
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        # Setando a Largura
        self.setMinimumWidth(MINIMUM_WIDTH)
        # Alinhando o texto para direita
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        # Colocando distancia nas margens
        self.setTextMargins(*margins)