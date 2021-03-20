from unittest import TestCase

from OO.carro import Motor


class CarroTestCase(TestCase): #herdando da classe testcase
    def teste_velocidade_inicial(self): #teste tem q começar com o prefixo test
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
