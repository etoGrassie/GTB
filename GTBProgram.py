from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QFileDialog


class GTBThread(QThread):
    def __init__(self):
        super(GTBThread, self).__init__()
        self.file_window()

    def file_window(self):
        window = QFileDialog.getOpenFileName(None, 'Open task a file', '.\\', 'Task File (*.tsk)')
        print(window)

    def file_open(self, path):
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