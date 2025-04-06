# Strategy (com funções de primeira classe)
def strategy_add(a, b):
    return a + b


def strategy_multiply(a, b):
    return a * b


class Calculator:
    def __init__(self, strategy=strategy_add):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy(a, b)


# Uso
calc = Calculator(strategy_multiply)
print(calc.execute(3, 4))  # 12


# Observer (com propriedades)
class Observable:
    def __init__(self):
        self._observers = []
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        for observer in self._observers:
            observer(new_value)

    def bind(self, observer):
        self._observers.append(observer)


# Uso
obs = Observable()
obs.bind(lambda x: print(f"Valor mudou para {x}"))
obs.value = 10  # Imprime "Valor mudou para 10"
