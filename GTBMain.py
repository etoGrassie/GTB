from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from qt_material import apply_stylesheet

from GTBTask import GTBProceed
from GTBProgram import GTBThread
from GTBWindow import Ui_GTBMainWindow


class GTBApp(QMainWindow, Ui_GTBMainWindow):
    signal_file_window = pyqtSignal()

    def __init__(self):
        super(GTBApp, self).__init__()
        self.setupUi(self)
        self.add_actions()

    def add_actions(self):
        self.pushButton_open_file.clicked.connect(self.emitter_open_file)

    def set_preview(self, text, path, task_count):
        self.textBrowser_file_preview.setPlainText(text)
        self.lineEdit_file_path.setText(path)
        if task_count == 1:
            self.commandLinkButton_run.setText('RUN {} TASK FROM FILE'.format(task_count))
            self.commandLinkButton_run.setEnabled(True)
        elif task_count >= 1:
            self.commandLinkButton_run.setText('RUN {} TASKS FROM FILE'.format(task_count))
            self.commandLinkButton_run.setEnabled(True)
        else:
            pass

    def emitter_open_file(self):
        self.signal_file_window.emit()

    @staticmethod
    def debug():
        print('self.debug active! ')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # For Dark
    apply_stylesheet(app, theme='dark_blue.xml')  # For Dark Blue Teal Default

    ui = GTBApp()
    thread = GTBThread()
    proceed = GTBProceed()
    ui.signal_file_window.connect(thread.file_window)
    thread.signal_file_window_return_text.connect(ui.set_preview)

    ui.show()

    sys.exit(app.exec_())

