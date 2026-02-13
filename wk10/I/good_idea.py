from abc import  abstractmethod

class Printer:#เครื่องพิมพ์
    @abstractmethod
    def print(self, document):
        pass
class Scanner:#เครื่องสแกน
    @abstractmethod
    def scan(self, document):
        pass
class Fax:#เครื่องแฟกซ์
    @abstractmethod
    def fax(self, document):
        pass
    
#เครื่องพิมพ์มัลติฟังก์ชัน
class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self, document):
        print("Printing document...")
    def scan(self, document):
        print("Scanning document...")
    def fax(self, document):
        print("Faxing document...")