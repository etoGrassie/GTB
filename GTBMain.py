from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5 import QtWidgets
from GTBWindow import Ui_GTBMainWindow


class GTBApp(Ui_GTBMainWindow, QMainWindow):
    signal_file_window = pyqtSignal()
    signal_file_window_return = pyqtSignal(str)

    def __init__(self):
        super(GTBApp, self).__init__()
        self.pushButton_open_file.clicked.connect(lambda: self.file_window(r'C:\Users\Administrator\Desktop\task.tsk'))

    def file_window(self, path):
        file_index = []
        with open(path, 'r') as file:
            file_index.append(file.readlines())
        self.textBrowser_file_preview.setPlainText(file_index)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    GTBMainWindow = QtWidgets.QMainWindow()
    ui = GTBApp()
    ui.setupUi(GTBMainWindow)
    GTBMainWindow.show()
    sys.exit(app.exec_())
