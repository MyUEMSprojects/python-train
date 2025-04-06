# 1. Fixtures (pytest)

import pytest


@pytest.fixture
def database_connection():
    conn = create_db_connection()
    yield conn  # Setup e teardown em um só
    conn.close()


def test_query(database_connection):
    result = database_connection.execute("SELECT 1")
    assert result == 1


# 2. Parametrização (pytest)
@pytest.mark.parametrize("input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42, marks=pytest.mark.xfail),
])
def test_eval(input, expected):
    assert eval(input) == expected


# 3. Mocking (unittest.mock)
from unittest.mock import patch


def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        response = call_api()
        assert response == 200

# Testes para Programadores C/C++
# test_extension.py
import my_cpp_extension


def test_cpp_function():
    assert my_cpp_extension.compute(3, 4) == 42

# 2. Benchmarks (pytest-benchmark)
def test_performance(benchmark):
    result = benchmark(my_cpp_extension.compute, 3, 4)
    assert result == 42

# 3. Integração com CMake/CTest
# CMakeLists.txt
find_package(Python REQUIRED)
add_test(
    NAME python_tests
    COMMAND ${Python_EXECUTABLE} -m pytest ${CMAKE_CURRENT_SOURCE_DIR}/tests
)

# Boas Práticas
projeto/
├── src/
├── tests/
│   ├── __init__.py
│   ├── test_unit.py
│   └── test_integration.py

#Nomenclatura:
#    Arquivos: test_*.py ou *_test.py
#    Funções: def test_*()

#Test Pyramid:
#    Muitos testes unitários
#    Alguns testes de integração
#    Poucos testes end-to-end

# Exemplo Completo (Sistema de Pagamentos)
# payment.py
class PaymentProcessor:
    def __init__(self, gateway):
        self.gateway = gateway
    
    def process(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return self.gateway.charge(amount)

from unittest.mock import Mock

# test_payment.py
import pytest


class TestPaymentProcessor:
    def test_positive_amount(self):
        gateway = Mock()
        processor = PaymentProcessor(gateway)
        gateway.charge.return_value = True
        assert processor.process(100) is True
    
    def test_invalid_amount(self):
        with pytest.raises(ValueError):
            processor = PaymentProcessor(Mock())
            processor.process(-1)

@pytest.fixture
def processor():
    gateway = Mock()
    gateway.charge.return_value = True
    return PaymentProcessor(gateway)

def test_processor_with_fixture(processor):
    assert processor.process(50) is True

# Exercício Prático

#   Implemente uma classe Calculator com:
#        add(a, b)
#        divide(a, b)
#        sqrt(x) (lança ValueError para x < 0)

#    Escreva testes usando pytest:
#        Teste operações básicas
#        Teste tratamento de erros
#        Use fixtures para o setup
#        Adicione parametrização

# Dica: Use pytest.raises para verificar exceções.
