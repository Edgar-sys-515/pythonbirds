
"""
Voce deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) motor
2) direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
1) Método acelerar, que deverá incrementar a velocidade de uma unidade
2) Método frenas, que deverá decrementar duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor em direção com valores possiveis: Norte, sul, leste, oeste
2) metodo girar_a_direita
3) metodo girar_a_esquerda

   N
 O   L
   S

Exemplo
>>> # Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
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
>>> motor.frear()
>>> motor.velocidade
0

>>> # Testando direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcula_velocidade()
0
>>> carro.acelerar()
>>> carro.calcula_velocidade()
1
>>> carro.frear()
>>> carro.calcula_velocidade()
0
>>> carro.calcula_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcula_direcao()
'Leste'
>>> carro.girar_a_direita()
>>> carro.calcula_direcao()
'Sul'
>>> carro.girar_a_direita()
>>> carro.calcula_direcao()
'Oeste'
>>> carro.girar_a_direita()
>>> carro.calcula_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcula_direcao()
'Oeste'
>>> carro.girar_a_esquerda()
>>> carro.calcula_direcao()
'Sul'
>>> carro.girar_a_esquerda()
>>> carro.calcula_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcula_direcao()
'Norte'
"""


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcula_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcula_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dict = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dict = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]



class Motor(object):
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

