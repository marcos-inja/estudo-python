# A classe é a "planta da casa"
class produto:
    def __init__(self, nome, preco=1.99, desc=0):
        # __ fez o nome ficar privado
        self.__nome = nome
        self.__preco = preco
        self.desc = desc

    # É usado para não dá pra passar nada no parâmetro (foi o que entendi kk)

    @property
    def nome(self):
        return self.__nome

    # Usado pra pegar o valor de preco

    @property
    def preco(self):
        return self.__preco

    # Usado para alterar o valor de preço

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    # Está senso usado para calcular o valor final

    @property
    def preco_final(self):
        # Coloca o 1 para ficar a porcentagem completa
        # por ex: 0.2 fica 0.8 que vai ser multiplicado pelo valor
        return (1 - self.desc) * self.preco


# Crio dois produtos
p1 = produto('Caneta', 5, 0.3)
p2 = produto('Caderno', 40, 0.5)

p1.preco = 4
p2.preco = 30
# Sem o @propety posso chamar o preco_final assim:
# print(p1.nome, p1.preco, p1.preco_final())

# Com o @propety só posso chamar o preco_final assim:
# É usado para não dá pra passar nada no parâmetro
print(p1.nome, p1.preco, p1.preco_final)
print(p2.nome, p2.preco, p2.preco_final)
