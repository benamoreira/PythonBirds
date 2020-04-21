from unittest import TestCase

def soma (a,b):
    return 4

class TestSoma(TestCase):
    def test_soma(self):
        resultado = soma(1,3)
        self.assertEqual(4, resultado)