# Se você vem de C++, pode pensar em metaclasses como:
# - Templates de templates (em C++ templates)
# - Um mecanismo para metaprogramação em tempo de compilação
# - Mas com muito mais flexibilidade e dinamismo

# Conceito Fundamental

# Em Python, tudo é objeto, incluindo classes. Metaclasses são as "classes das classes"
# que controlam como as classes são criadas.


class MinhaClasse:
    pass


print(type(MinhaClasse))  # <class 'type'>

# Como Funciona a Criação de Classes
# - Quando você define uma classe, Python chama type(name, bases, namespace)
# - Você pode customizar esse processo criando sua própria metaclasse


# Criando uma Metaclasse Básica
class MinhaMeta(type):
    def __new__(mcls, name, bases, namespace):
        print(f"Criando classe {name}")
        namespace["version"] = 1.0  # Adiciona atributo à classe
        return super().__new__(mcls, name, bases, namespace)


class MinhaClasse(metaclass=MinhaMeta):
    pass


print(MinhaClasse.version)  # 1.0


# Casos de Uso Reais
# 1. Registro Automático de Classes
class PluginRegistry(type):
    _plugins = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if not name.startswith("Base"):
            mcls._plugins[name.lower()] = cls
        return cls


class BasePlugin(metaclass=PluginRegistry):
    pass


class DataProcessor(BasePlugin):
    pass


class ImageProcessor(BasePlugin):
    pass


print(PluginRegistry._plugins)
# {'dataprocessor': <class '__main__.DataProcessor'>,
#  'imageprocessor': <class '__main__.ImageProcessor'>}


# 2. Validação de Atributos
class ValidatedFields(type):
    def __new__(mcls, name, bases, namespace):
        # Valida campos marcados com _validate
        for attr_name, attr_value in namespace.items():
            if hasattr(attr_value, "_validate"):
                if not isinstance(attr_value._default, attr_value._type):
                    raise TypeError(
                        f"{attr_name} deve ser {attr_value._type.__name__}, "
                        f"obteve {type(attr_value._default).__name__}"
                    )
        return super().__new__(mcls, name, bases, namespace)


def validate_field(type_, default):
    field = type("Field", (), {"_type": type_, "_default": default, "_validate": True})
    return field()


class Person(metaclass=ValidatedFields):
    name = validate_field(str, "John")
    age = validate_field(int, 30)
    # age = validate_field(int, "30")  # TypeError


p = Person()
print(p.name, p.age)  # John 30


# 3. Singleton Pattern
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Criando conexão com o banco")


db1 = Database()
db2 = Database()
print(db1 is db2)  # True


# Exemplo Avançado: ORM Simples
class Field:
    def __init__(self, type_, primary_key=False):
        self.type_ = type_
        self.primary_key = primary_key


class ModelMeta(type):
    def __new__(mcls, name, bases, namespace):
        fields = {}
        for k, v in namespace.items():
            if isinstance(v, Field):
                fields[k] = v

        namespace["_fields"] = fields
        namespace["_tablename"] = name.lower()

        return super().__new__(mcls, name, bases, namespace)


class Model(metaclass=ModelMeta):
    @classmethod
    def create_table_sql(cls):
        columns = []
        for name, field in cls._fields.items():
            col = f"{name} {field.type_.__name__}"
            if field.primary_key:
                col += " PRIMARY KEY"
            columns.append(col)
        return f"CREATE TABLE {cls._tablename} ({', '.join(columns)})"


class User(Model):
    id = Field(int, primary_key=True)
    name = Field(str)
    age = Field(int)


print(User.create_table_sql())
# CREATE TABLE user (id int PRIMARY KEY, name str, age int)

# Quando Não Usar Metaclasses
# - Quando decorators são suficientes
# - Para problemas simples de herança
# - Se reduzir a legibilidade do código
# - Se você não é o mantenedor do código

# Exercício Prático
# Implemente uma metaclasse AutoSerializable que:
# - Automaticamente adiciona um método to_dict() que retorna todos os atributos da instância
# - Adiciona um método de classe from_dict() que recria a instância


class AutoSerializable(type):
    def __new__(mcls, name, bases, namespace):
        # Implemente aqui
        pass


class Person(metaclass=AutoSerializable):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alice", 30)
d = p.to_dict()
print(d)  # {'name': 'Alice', 'age': 30}

p2 = Person.from_dict(d)
print(p2.name, p2.age)  # Alice 30
