# Dicas para Desenvolvedores C/C++
# ctypes: Para integrar bibliotecas C existentes
from ctypes import CDLL

lib = CDLL('./mylib.so')

# Cython: Para escrever extensões em Python-like syntax
def fib(int n):
    cdef int a=0, b=1, i
    for i in range(n):
        a, b = b, a+b
    return a

# pybind11: Para criar bindings C++ de alta qualidade
PYBIND11_MODULE(example, m) {
    m.def("add", [](int a, int b) { return a + b; });
}
