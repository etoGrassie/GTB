from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from qt_material import apply_stylesheet

from GTBWindow import Ui_GTBMainWindow


# import qdarkstyle

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
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # For Dark
    apply_stylesheet(app, theme='dark_teal.xml')  # For Dark Teal

    ui = GTBApp()
    ui.show()

    sys.exit(app.exec_())
