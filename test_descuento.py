import unittest
from validador_contrasena import validar_contrasena

def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio final aplicando un porcentaje de descuento.
    """
    return round(precio * (1 - porcentaje / 100), 5)

class TestCalcularDescuento(unittest.TestCase):
    def test_descuento_20_por_ciento(self):
        self.assertEqual(calcular_descuento(100, 20), 80)

    def test_descuento_0_por_ciento(self):
        self.assertEqual(calcular_descuento(100, 0), 100)

    def test_descuento_100_por_ciento(self):
        self.assertEqual(calcular_descuento(100, 100), 0)

    def test_descuento_decimal(self):
        self.assertEqual(calcular_descuento(99.99, 15), 84.9915)

    def test_descuento_valor_cero(self):
        self.assertEqual(calcular_descuento(0, 50), 0)

if __name__ == "__main__":
    unittest.main()
