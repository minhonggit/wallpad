from PyQt5 import QtCore, QtGui, QtWidgets, uic
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, qApp

class MainWindow(Ui_MainWindow):
    def __init__(self, w):
        Ui_MainWindow.__init__(self)
        self.setupUi(w)

        label1 = self.label
        label2 = self.label_2
        pixmap = QtGui.QPixmap('Infra.png')
        pixmap2 = QtGui.QPixmap('Device.png')
        label1.setPixmap(pixmap)
        label2.setPixmap(pixmap2)

class ListWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = uic.loadUi('listing.ui',self)
        self.show()

class CheckingWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = uic.loadUi('checking.ui',self)
        self.show()

class ResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = uic.loadUi('result.ui',self)
        self.show()

class DetailWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = uic.loadUi('detail.ui',self)


        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = DetailWindow()
    ui = ResultWindow()
    ui = CheckingWindow()
    ui = ListWindow()

    w = QtWidgets.QMainWindow()
    ui = MainWindow(w)
    w.show()

    sys.exit(app.exec_())


