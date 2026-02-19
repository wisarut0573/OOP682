import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from services.factory import SourceFactory # เรียกใช้ Factory

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # เปลี่ยนมาใช้ csv source ผ่าน factory
    log = SourceFactory.create_source("csv", "logs/voters.csv")
    
    viewer = MainWindow(log)
    viewer.show()
    sys.exit(app.exec())