from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
import sys
from Multiplayer_chess import *


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.Multiplayer_window = MainWindow()
        uic.loadUi('UILauncher.ui', self)
        self.show()
        self.ImageLabel.setPixmap(QPixmap('Launcher.jpg'))
        self.Multiplayer_pushButton.clicked.connect(self.multiplayerPressed)
        self.dialog = MainWindow()

    def multiplayerPressed(self):
        self.Multiplayer_window.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
