from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from qt_material import apply_stylesheet

from GTBWindow import Ui_GTBMainWindow


# import qdarkstyle

class GTBApp(QMainWindow, Ui_GTBMainWindow):
    signal_file_window = pyqtSignal()
    signal_file_window_return = pyqtSignal(list)

    def __init__(self):
        super(GTBApp, self).__init__()
        self.setupUi(self)
        self.add_actions()

    def add_actions(self):
        self.pushButton_open_file.clicked.connect(lambda: self.file_window(r'C:\Users\Administrator\Desktop\task.tsk'))

    def debug(self):
        print('self.debug active! ')

    def file_window(self, path):
        file_index = []
        file_text = ''
        with open(path, 'r') as file:
            for task in file.readlines():
                file_text += task
            file_index.extend(file.readlines())

            for task in file:
                file_index.append(file.readline())
        self.textBrowser_file_preview.setPlainText(file_text)
        self.signal_file_window_return.emit(file_index)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # For Dark
    apply_stylesheet(app, theme='dark_teal.xml')  # For Dark Teal

    ui = GTBApp()
    ui.show()

    sys.exit(app.exec_())
