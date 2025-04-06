# Não pythonico (acoplado)
class DataProcessor:
    def __init__(self):
        self.db = PostgreSQLDatabase()


# Pythonico (injetado)
class DataProcessor:
    def __init__(self, db):
        self.db = db


# Uso
processor = DataProcessor(SQLiteDatabase())
