from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from qt_material import apply_stylesheet

from GTBWindow import Ui_GTBMainWindow


class GTBApp(QMainWindow, Ui_GTBMainWindow):
    signal_file_window = pyqtSignal()
    signal_file_window_return = pyqtSignal(list)

    def __init__(self):
        super(GTBApp, self).__init__()
        self.setupUi(self)
        self.add_actions()

    def add_actions(self):
        self.pushButton_open_file.clicked.connect(self.file_window)



    @staticmethod
    def debug():
        print('self.debug active! ')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # For Dark
    apply_stylesheet(app, theme='dark_blue.xml')  # For Dark Blue Teal Default

    ui = GTBApp()
    ui.show()

    sys.exit(app.exec_())
