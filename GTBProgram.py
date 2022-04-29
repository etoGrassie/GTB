from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QFileDialog


class GTBThread(QThread):
    signal_file_window_return_index = pyqtSignal(list)
    signal_file_window_return_text = pyqtSignal(str, str, int)

    def __init__(self):
        super(GTBThread, self).__init__()

    def file_window(self):
        window = QFileDialog.getOpenFileName(None, 'Open task a file', '.\\', 'Task File (*.tsk)')
        if bool(window[0]) is True:
            self.file_open(window[0])
        else:
            return

    def file_open(self, path):
        file_index = []
        file_text = ''
        with open(path, 'r') as file:
            for task in file.readlines():
                file_text += task
                file_index.append(task)
            for task in file.readlines():
                file_index.append(task)

        self.signal_file_window_return_index.emit(file_index)
        self.signal_file_window_return_text.emit(file_text, path, len(file_index))
        print(file_index)
