nota = float(input('Informe a nota do aluno 1: '))
comportado = True if input('Comportado (s/n)') == 's' else False

if nota >= 9:
    if comportado:
        print('Quadro de honra!')

    print('Para béns! kkk')

elif nota >= 7:
    print('Passou')

elif nota >= 4:
    print('Recuperação')
    
else:
    print('Sem jeito')


print(nota)
