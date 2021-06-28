import chess
import chess.svg
from PyQt5.QtGui import QFont
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import pyqtSlot, Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 800, 875)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 775, 775)
        self.board = chess.Board()

        self.boardSize = min(self.widgetSvg.width(),
                             self.widgetSvg.height())
        self.coordinates = False
        self.margin = 0.05 * self.boardSize if self.coordinates else 0
        self.squareSize = (self.boardSize - 2 * self.margin) / 8.0
        self.pieceToMove = [None, None]

        self.boardSvg = chess.svg.board(self.board).encode("UTF-8")
        self.widgetSvg.load(self.boardSvg)
        self.label1 = QLabel(self)
        self.label1.move(10, 800)
        self.label1.resize(775, 50)
        self.label1.setStyleSheet("border: 5px solid black;")
        self.label1.setFont(QFont('Arial', 25))

    @pyqtSlot(QWidget)
    def mousePressEvent(self, event):
        if self.board.is_checkmate():
            a = chess.Color
            self.label1.setText("CheckMate!, Game over")
        else:
            if event.x() <= self.boardSize and event.y() <= self.boardSize:
                if event.buttons() == Qt.LeftButton:
                    if self.margin < event.x() < self.boardSize - self.margin and self.margin < event.y() < self.boardSize - self.margin:
                        file = int((event.x() - self.margin) / self.squareSize)
                        rank = 7 - int((event.y() - self.margin) / self.squareSize)
                        square = chess.square(file, rank)
                        piece = self.board.piece_at(square)
                        coordinates = "{}{}".format(chr(file + 97), str(rank + 1))
                        if self.pieceToMove[0] is not None:
                            move = chess.Move.from_uci("{}{}".format(self.pieceToMove[1], coordinates))
                            if move in self.board.legal_moves:
                                self.board.push(move)
                                if self.board.is_check():
                                    self.label1.setText("Check!")
                                else:
                                    self.label1.setText("")
                            piece = None
                            coordinates = None
                        self.pieceToMove = [piece, coordinates]
                        self.boardSvg = chess.svg.board(self.board).encode("UTF-8")
                        self.widgetSvg.load(self.boardSvg)
