# Adapter (usando classes ou funções)
class EuropeanSocket:
    def voltage(self):
        return 230


class USAdapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return self.socket.voltage() / 2


# Uso
euro_socket = EuropeanSocket()
us_adapter = USAdapter(euro_socket)
print(us_adapter.voltage())  # 115


# Decorator (nativo em Python)
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Tempo: {time.time() - start:.2f}s")
        return result

    return wrapper


@log_time
def heavy_computation():
    time.sleep(1)


heavy_computation()
