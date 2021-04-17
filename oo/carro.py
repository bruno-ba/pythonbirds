"""
Exemplo:

>>> motor = Motor()
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> direcao = Direcao()
>>> direcao.valor
'NORTE'
>>> direcao.girar_direita()
>>> direcao.valor
'LESTE'
>>> direcao.girar_direita()
>>> direcao.valor
'SUL'
>>> direcao.girar_direita()
>>> direcao.valor
'OESTE'
>>> direcao.girar_direita()
>>> direcao.valor
'NORTE'
>>> direcao.girar_esquerda()
>>> direcao.valor
'OESTE'
>>> direcao.girar_esquerda()
>>> direcao.valor
'SUL'
>>> direcao.girar_esquerda()
>>> direcao.valor
'LESTE'
>>> direcao.girar_esquerda()
>>> direcao.valor
'NORTE'
>>> direcao = Direcao()
>>> motor = Motor()
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'NORTE'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'LESTE'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    direcoes = ['NORTE', 'LESTE', 'SUL', 'OESTE']

    def __init__(self):
        self.current_index = 0
        self.valor = Direcao.direcoes[0]

    def girar_direita(self):
        self._girar_index(+1)
        self.valor = Direcao.direcoes[self.current_index]

    def girar_esquerda(self):
        self._girar_index(-1)
        self.valor = Direcao.direcoes[self.current_index]

    def _girar_index(self, num):
        self.current_index = (self.current_index + num) % len(Direcao.direcoes)


class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def acelerar(self):
        self.motor.acelerar()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_esquerda()


