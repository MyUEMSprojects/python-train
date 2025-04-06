# Context Manager (with statement)
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect_to_db()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


# Uso
with DatabaseConnection() as conn:
    conn.execute_query("SELECT ...")


# Descriptor (para propriedades gerenciadas)
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Valor deve ser positivo")
        obj.__dict__[self.name] = value


class Account:
    balance = PositiveNumber()


acc = Account()
acc.balance = 100  # Ok
# acc.balance = -50  # ValueError
