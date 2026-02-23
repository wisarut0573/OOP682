import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from services.factory import SourceFactory
from services.filters import ErrorOnlyFilter

if __name__ == "__main__":
    app = QApplication(sys.argv)

    source = SourceFactory.create_source("csv") 
    window = MainWindow(source)
    
    # window.set_filter_strategy(ErrorOnlyFilter())

    window.show()
    sys.exit(app.exec())