import chess
import chess.svg
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 800, 800)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 775, 775)
        self.board = chess.Board()
        self.boardSvg = chess.svg.board(self.board).encode("UTF-8")
        self.widgetSvg.load(self.boardSvg)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()