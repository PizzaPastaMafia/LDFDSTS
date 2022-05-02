import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GUI(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Lorenzo Del Forno Dynamic Stock Trading Simulator')
        
        mainFrame = QHBoxLayout()
        mainFrame.setStyleSheet("background:white")

        leftSide = QVBoxLayout()
        leftSide.setStyleSheet("background:blue")

        stockGeneral = QVBoxLayout()
        stockGeneral.setStyleSheet("background:yellow")

        stockAdvanced = QVBoxLayout()
        stockGeneral.setStyleSheet("background:red")

        mainFrame.setLayout(leftSide)
        mainFrame.setLayout(stockGeneral)
        mainFrame.setLayout(stockAdvanced)

        
        self.setLayout(mainFramw)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = GUI()
    dlg.show()
    sys.exit(app.exec_())