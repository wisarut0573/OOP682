from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MySQL database...")
    
class PostgreSQLDatabase(Database):
    def save(self, data):
        print("Saving data to PostgreSQL database...")

class App:
    def __init__(self, database: Database):
        #App พึ่งพาอาศัย Database abstraction 
        #แทนที่จะผูกมัดกับ MySQLDatabase โดยตรง
        self.database = database

    def save_data(self, data):
        self.database.save(data)