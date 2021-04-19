from unittest import TestCase
from oo.carro import Motor


class CarroTestCase(TestCase):

    def teste_velociade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)