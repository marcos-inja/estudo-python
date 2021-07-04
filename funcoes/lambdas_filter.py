from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 8.3},
    {'nome': 'João', 'nota': 6.7},
    {'nome': 'José', 'nota': 5.2},
    {'nome': 'Marcos', 'nota': 9},
    {'nome': 'Max', 'nota': 6.3},
    {'nome': 'Júlia', 'nota': 7.5}
]

# Aqui é uma função anônima ele está retornando True caso nota seja maior que 7
aluno_aprovado = lambda aluno: aluno['nota']>= 7
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b
media = lambda a, b: a / b


print(obter_nota(alunos[2]))

# Aqui usa o list para ser legivél para humanos
# Usa o filter para criar um novo array, passando a função de cima e o que vai ser filtrado
# Em JS faz o filter ao contrário
alunos_aprovados = list(filter(aluno_aprovado, alunos))

# Pega as notas dos alunos aprovados
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
# Usando o reduce para pegar o total das notas somadas
total = reduce(somar,notas_alunos_aprovados, 0)

# O que vale é que eu usei o reduce kkkk
# Passo o reduce, e o tamanho dele na média
m = media(reduce(somar, notas_alunos_aprovados, 0), len(notas_alunos_aprovados))

print(alunos)
print(alunos_aprovados)
print(notas_alunos_aprovados)
print(m)
