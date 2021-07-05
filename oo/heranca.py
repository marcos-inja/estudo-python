# Defino o básico
class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade

    def frear(self):
        if self.__velocidade >= 5:
            self.__velocidade -= 5
        return self.__velocidade


# Herda a classe
class Uno(Carro):
    pass


# A Ferrari acelera mais rapidamente
class Ferrari(Carro):
    def acelerar(self):
        # Uso o super() para chamar algo da classe mãe
        super().acelerar()
        return super().acelerar()


c1 = Uno()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.velocidade)
