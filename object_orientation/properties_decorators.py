# Vindo de C++, você pode pensar em properties como uma versão mais poderosa
# e flexível dos getters/setters, e decorators como uma forma avançada de
# metaprogramação que modifica funções/classes em tempo de definição.


# Conceito básico:
# As properties permitem que você defina métodos que são acessados como atributos:
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Atributo "privado" (convenção)

    @property
    def radius(self):
        """Getter para o raio"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter para o raio com validação"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        """Propriedade calculada (somente leitura)"""
        return 3.14159 * self._radius**2


# Uso
c = Circle(5)
print(c.radius)  # 5 (chama o getter)
c.radius = 10  # Chama o setter
print(c.area)  # 314.159 (somente leitura)
# c.area = 50    # AttributeError


# Decorators (Funções que Decoram outras funções)
# Conceito Básico
# Decorators são funções que modificam o comportamento de outras funções/métodos
def log_time(func):
    """Decorator que loga o tempo de execução"""

    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} executou em {time.time() - start:.4f}s")
        return result

    return wrapper


@log_time
def calculate_something(n):
    return sum(i * i for i in range(n))


# Equivalente a:
# calculate_something = log_time(calculate_something)

# Decorators uteis da lib padrão
# @property - Já visto
# @classmethod - Método de classe (recebe cls em vez de self)
# @staticmethod - Método estático (não recebe self nem cls)
# @functools.lru_cache - Cache de resultados
# @dataclass.dataclass - Já visto anteriormente

# Exemplo avançado com parametros


def retry(max_attempts=3, delay=1):
    """Decorator com parâmetros que tenta executar novamente em caso de falha"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    print(f"Falha (tentativa {attempts}/{max_attempts}): {e}")
                    import time

                    time.sleep(delay)

        return wrapper

    return decorator


@retry(max_attempts=5, delay=2)
def fetch_data(url):
    # Simula falha aleatória
    import random

    if random.random() < 0.7:
        raise ConnectionError("Falha na conexão")
    return "Dados importantes"


print(fetch_data("http://example.com"))

# Padrão de Projeto: Decorator Class
# Voce também pode implmenetar decorators como classes:


class CountCalls:
    """Decorator que conta quantas vezes uma função foi chamada"""

    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Chamada {self.calls} de {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello!")


say_hello()  # Chamada 1 de say_hello
say_hello()  # Chamada 2 de say_hello

# Caso real: Sistema de Caching
import functools
import time


def cached_property(func):
    """Cacheia o resultado de uma propriedade (uma vez por instância)"""

    @functools.wraps(func)
    def wrapper(self):
        cache_attr = f"_cached_{func.__name__}"
        if not hasattr(self, cache_attr):
            setattr(self, cache_attr, func(self))
        return getattr(self, cache_attr)

    return property(wrapper)


class DatabaseConnection:
    def __init__(self, dsn):
        self.dsn = dsn
        self._connection = None

    @cached_property
    def connection(self):
        """Conexão cara que só deve ser feita uma vez"""
        print("Estabelecendo conexão...")
        time.sleep(2)  # Simula operação demorada
        return f"Connection to {self.dsn}"


db = DatabaseConnection("postgres://user:pass@localhost")
print(db.connection)  # Demora
print(db.connection)  # Retorna imediatamente


# Exericio Prática
# implementa um sistema de permissões usando properties e decorators:
class User:
    def __init__(self, username, role):
        self.username = username
        self._role = role
        self._permissions = {
            "admin": ["create", "read", "update", "delete"],
            "editor": ["read", "update"],
            "viewer": ["read"],
        }

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, new_role):
        if new_role not in self._permissions:
            raise ValueError("Função inválida")
        self._role = new_role

    def check_permission(self, action):
        return action in self._permissions[self.role]


def requires_permission(action):
    """Decorator que verifica permissão antes de executar"""

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not self.check_permission(action):
                raise PermissionError(f"Ação '{action}' não permitida para {self.role}")
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


class Document:
    def __init__(self, content):
        self.content = content

    @requires_permission("read")
    def view(self):
        print(f"Conteúdo: {self.content}")

    @requires_permission("update")
    def edit(self, new_content):
        self.content = new_content
        print("Documento atualizado")


# Teste
user = User("admin_user", "admin")
doc = Document("Segredo")
doc.view()  # OK
doc.edit("Novo segredo")  # OK

user.role = "viewer"
doc.view()  # OK
doc.edit("Tentativa")  # PermissionError
