class Contador:
    contador = 0

    def inst(self):
        return 'Tuuruururru'

    def contador_m(self):
        # Aqui ele está criando um novo contador
        self.contador += 1
        return self.contador

    # O @classmethod eo @staticmethod não precisam de instâcia
    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador
    
    @classmethod
    def dec(cls):
        if cls.contador >= 1:
            cls.contador -= 1
        return cls.contador

    @staticmethod
    def mais_um(n):
        return n + 1

# Quando eu declaro assim o conteudo não é alterdo, 
# por isso o metodo da classe retorna algo novo
c1 = Contador()
print(c1.inst())
print(c1.contador_m())

# Como esses metódos inc e dec pertencem a classe posso chamar assim:
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.mais_um(99))

# Já com o metódo inst não posso chamr assim tenho que declarar uma instância:
# Aqui ele só pega o que já existe em c1
print(c1.inst())
print(c1.contador_m())
