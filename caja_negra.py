import unittest

def suma_dos_positivos(x,y):
    return x+y

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10 
        num_2 = 20

        resultado = suma_dos_positivos(num_1,num_2)

        self.assertEqual(resultado, 30)

if __name__ == '__main__':
    unittest.main()