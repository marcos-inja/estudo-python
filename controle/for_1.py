# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 100, 7): # vai de 1 a 99 de 7 em 7
#     print(i)

# for i in range(20, 0, -2): # vai de 20 a 0 de -2 em -2
#     print(i)

# nums = [1, 2, 3, 4, 5, 6]

# for n in nums:  # com isso percorre todo o array
#     print(n, end=' ') # O end é o segundo paramtro do print o padrão é \n

# texto = 'Python é muito massa!'

# for letra in texto:
#     print(letra, end='\n\n') # vai pular de duas em duas linhas

# for i in {1, 2, 3, 4}:
#     print(i, end=' ')

produto = {
    'nome': 'Camisa',
    'preco': 30.88,
    'desc': 0.4
}

# for p in produto:
#     print(p, '=>', produto[p])

# for p, valor in produto.items():
#     print(p, '=>', valor)

for valor in produto.values():  # Pega só os valores
    print(valor)

print('')  #Dá um espaço

for atrib in produto.keys():  # Pega só os atributos
    print(atrib)


