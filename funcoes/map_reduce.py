from functools import reduce


# Está sendo usado para as notas não passarem de 10
def limitar_notas(num):
    if num > 10:
        num = 10
    return num


# Com valor que vai ser adicionado fixo:
def mais_um_meio(nota):
    nota = limitar_notas(nota + 1.5)
    return nota


# com o valor que vai ser adicionado não fixo e usando a programação funcional
def somar_nota(delta):
    def calc(nota):
        nota = limitar_notas(nota + delta)
        return nota
    return calc


notas = [5.6, 7.5, 7.8, 9.6]
# Colocar um list para retorno ser em números
notas_finais = list(map(somar_nota(1.7), notas))
notas_finais1 = list(map(somar_nota(3), notas))

print(notas_finais)
print(notas_finais1)


# Soma tudo que for colocado aqui dentro haha
def somar(a, b):
    return a + b

# Usando o reduce, o zero é o valor inicial
total = reduce(somar, notas_finais, 0)
print(total)

# Forma bruta
# total = 0
# for n in notas_finais1:
#     total += n

# print(total)

# Posso fazer isso dessas duas formas:
# for i, nota in enumerate(notas):
#     notas[i] = limitar_notas(nota + 1.5)

# Esse é metódo bruto kkk
# for i in range(len(notas)):
#     notas[i] = limitar_notas(notas[i] + 1.5)

# print(notas)
