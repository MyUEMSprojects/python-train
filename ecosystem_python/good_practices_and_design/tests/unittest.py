# Se você vem de C++, pode pensar nos frameworks de teste Python como:
#    unittest ≈ Google Test (xUnit style)
#    pytest ≈ Catch2 (mais moderno e conciso)

# Vamos explorar os dois principais frameworks de teste em Python:
# 1. unittest (Biblioteca Padrão)
# Similar ao Google Test (C++):

import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()

#Principais asserts:
#    self.assertEqual(a, b)
#    self.assertTrue(x)
#    self.assertRaises(Error)
#    self.assertIn(a, b)

# Execução:
python -m unittest test_module.py


