# Exemplo básico de herança


class A:
    def metodo(self):
        print("A")


class B(A):
    def metodo(self):
        print("B")
        super().metodo()


class C(A):
    def metodo(self):
        print("C")
        super().metodo()


class D(B, C):
    def metodo(self):
        print("D")
        super().metodo()


d = D()
d.metodo()

# Method Resolution Order (MRO)
# Python usa o algoritmo C3 para determinar a ordem de busca de métodos:
print(D.mro())  # Ou D.__mro__
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Regras do C3:
# - Filhos vem antes dos pais
# - A ordem das classes base é preservada
# - Para cada classe na herança, seus pais aparecem na ordem correta


# Mixins (Padrão Pythonico)
# Mixins são classes projetadas especificamente para herança multipla, adicionando comportamentos sem ser uma classe "principal".

# Caracteristicas de um bom mixin:
# - Não deve ter estado próprio (__init__)
# - Deve usar super() corretamente
# - Geralmente pequeno e focado
#


class JsonSerializableMixin:
    def to_json(self):
        import json

        return json.dumps(self.__dict__)


class XmlSerializableMixin:
    def to_xml(self):
        from xml.etree.ElementTree import Element, tostring

        el = Element(self.__class__.__name__)
        for k, v in self.__dict__.items():
            child = Element(k)
            child.text = str(v)
            el.append(child)
        return tostring(el)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class PessoaJson(Pessoa, JsonSerializableMixin):
    pass


class PessoaXmlJson(Pessoa, XmlSerializableMixin, JsonSerializableMixin):
    pass


p = PessoaJson("João", 30)
print(p.to_json())

p2 = PessoaXmlJson("Maria", 25)
print(p2.to_xml())
print(p2.to_json())

# Boas práticas
# 1) Prefira composição sobre herança (mas uando usar herança):
#    - Use mixins para funcionalidades transversais
#    - Mantenha hierarquias de herança rasas
#
# 2) Sempre usar super()
#    - Garanta que toda cadeia ded herança seja chamada
#    - Funciona mesmo com herança multipla
#
# 3) Documente o MRO esperado
#    - Especialmente
#


# Caso real: Django Class-based Views
class LoginRequiredMixin:
    """Verifica se o usuário está logado"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


class MyView(LoginRequiredMixin, View):
    """View protegida que requer login"""

    def get(self, request):
        return HttpResponse("Conteúdo protegido")


# Exercicio Avançado
# Implemente um sistema de permissões usando mixins
class Permission:
    def __init__(self, name):
        self.name = name


class HasPermissionsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._permissions = set()

    def add_permission(self, permission):
        self._permissions.add(permission)

    def has_permission(self, permission_name):
        return any(p.name == permission_name for p in self._permissions)


class AdminOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission("admin"):
            raise PermissionError("Admin required")
        return super().dispatch(request, *args, **kwargs)


# Implemente uma classe User que usa esses mixins
# E uma View que requer privilégios de admin
