# Como desenvolvedor C/C++, você já deve estar familiarizado
# com os padrões de projeto clássicos do GoF.
# Em Python, muitos desses padrões são implementados de forma mais simples e idiomática.
# Vamos explorar as principais diferenças e implementações pythonicas:


# Singleton (Pythonico)
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Uso
a = Singleton()
b = Singleton()
print(a is b)  # True


# Comparação C++: Em Python, o __new__ controla a criação de instâncias,
# similar ao operador new em C++, mas mais flexível.


# Factory Method (com funções)
def create_connection(protocol):
    if protocol == "http":
        return HttpConnection()
    elif protocol == "websocket":
        return WebSocketConnection()
    raise ValueError(f"Protocolo desconhecido: {protocol}")


# Uso
conn = create_connection("http")
