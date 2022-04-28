from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5 import QtWidgets
from GTBWindow import Ui_GTBMainWindow
from qt_material import apply_stylesheet

class GTBApp(QMainWindow, Ui_GTBMainWindow):
    signal_file_window = pyqtSignal()
    signal_file_window_return = pyqtSignal(str)

    def __init__(self):
        super(GTBApp, self).__init__()
        self.setupUi(self)
        self.add_actions()

    def add_actions(self):
        self.debug()
        self.pushButton_open_file.clicked.connect(self.debug)

    def debug(self):
        print('self.debug active! ')

    def file_window(self, path):
        print('DEBUG')
        file_index = []
        with open(path, 'r') as file:
            file_index.append(file.readlines())
        self.textBrowser_file_preview.setPlainText(file_index)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    ui = GTBApp()
    ui.show()

    sys.exit(app.exec_())
