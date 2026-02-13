from interfaces.data_source import ILogSource
from pyqt5.QtWidgets import QMainWindow, QTextEdit 

class MainWindow(MainWindow):
    def __init__(self, log_source):
        super().__init__()
        self.log_display = QTextEdit(self)
        self.log_resize(800, 600)
        self.setCentralWidget(self.log_display)
        self.log_display.setReadOnly(True)
        self.log_source = log_source
        self.load_logs()
        self.show()


    def load_logs(self):
        logs = self.log_source.get_logs()
        self.log_display.setText("\n".join(logs))