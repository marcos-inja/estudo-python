from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 8.3},
    {'nome': 'João', 'nota': 6.7},
    {'nome': 'José', 'nota': 5.2},
    {'nome': 'Marcos', 'nota': 9},
    {'nome': 'Max', 'nota': 6.3},
    {'nome': 'Júlia', 'nota': 7.5}
]

somar = lambda a, b: a + b

# Limitando o que vai ser pego nas váriaveis dentro dos colchetes
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 5]
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
nomes_alunos_aprovados = [aluno['nome'] for aluno in alunos_aprovados]

print(f'{alunos_aprovados}\n{notas_alunos_aprovados}\n{nomes_alunos_aprovados}')

# Passando alunos aprovados para imprimir sem nada
for i in range(len(alunos_aprovados)):
    print(f'{nomes_alunos_aprovados[i]}: {notas_alunos_aprovados[i]}')

total = reduce(somar,notas_alunos_aprovados, 0)

print(f'média: {total / len(alunos_aprovados)}')
