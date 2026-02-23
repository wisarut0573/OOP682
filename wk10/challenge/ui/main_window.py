from PySide6.QtWidgets import QMainWindow, QListWidget, QVBoxLayout, QWidget, QPushButton
from interfaces.data_source import ILogSource
from interfaces.strategy import IFilterStrategy
from services.filters import NoFilter

class MainWindow(QMainWindow):
    def __init__(self, source: ILogSource):
        super().__init__()
        self.source = source
        self.filter_strategy: IFilterStrategy = NoFilter()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Log Viewer Architecture")
        self.resize(400, 300)
        
        self.list_widget = QListWidget()
        btn_load = QPushButton("Load Logs")
        btn_load.clicked.connect(self.load_data)

        layout = QVBoxLayout()
        layout.addWidget(btn_load)
        layout.addWidget(self.list_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def set_filter_strategy(self, strategy: IFilterStrategy):
        self.filter_strategy = strategy

    def load_data(self):
        self.list_widget.clear()
        
        raw_logs = self.source.get_logs()
        filtered_logs = self.filter_strategy.filter(raw_logs)
        
        self.list_widget.addItems(filtered_logs)