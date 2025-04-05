# 2. pytest (Framework Moderno)
# Mais conciso e poderoso:
# test_sample.py
def test_upper():
    assert "foo".upper() == "FOO"


def test_isupper():
    assert "FOO".isupper()
    assert not "Foo".isupper()


def test_split():
    s = "hello world"
    assert s.split() == ["hello", "world"]
    with pytest.raises(TypeError):
        s.split(2)

#Vantagens do pytest:
#    Sintaxe mais limpa (sem classes obrigatórias)
#    Mensagens de erro mais descritivas
#    Muitos plugins úteis
#    Fixtures (dependências reutilizáveis)

# Execução:

pytest test_sample.py -v
