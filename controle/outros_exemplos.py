pessoas = ['Julia', 'Rebeca']
adjs = ['Doida', 'Inteligente']

for p  in pessoas:
    for a in adjs:
        print (f'{p} é {a}')

for i in pessoas:
    pass #vazio não funciona para variáveis

for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)

for i in range(1, 11):
    if i == 5:
        break
    print(i)
