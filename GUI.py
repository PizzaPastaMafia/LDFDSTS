import sys

# 1. Import `QApplication` and all the required widgets
#from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWidgets import QDialog
#from PyQt5.QtWidgets import QDialogButtonBox
#from PyQt5.QtWidgets import QFormLayout
#from PyQt5.QtWidgets import QLineEdit
#from PyQt5.QtWidgets import QVBoxLayout
#from PyQt5.QtWidgets import QHBoxLayout
#from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFrame, QMainWindow, QApplication, QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import  QPalette, QColor

import PyQt5

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        bg = QWidget(QFrame(None))
        bg.setStyleSheet("background-color: yellow;")
        layout2.addWidget(bg)
        layout2.addWidget()
        layout2.addWidget()

        layout1.addLayout( layout2 )

        layout1.addWidget()

        layout3.addWidget()
        layout3.addWidget()

        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())