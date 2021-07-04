# import pacote.sub.arquivo # Usado para importar

# duas formas de fazer a mesma coisa:
# import tipos.variaveis # pode importar assim
# from tipos import variaveis # E também pode importar assim

# from tipos import variaveis, basicos # posso chamr varios de uma vez colocando virgúla

# import tipos.lista
# import tipos.tuplas
# import tipos.conjuntos
# import tipos.dicionario

# import operadores.unarios
# import operadores.aritmeticos
# import operadores.relacionais
# import operadores.atribuicao
# import operadores.logicos
# import operadores.ternario

# import controle.if_1
# import controle.if_2
# import controle.for_1
# import controle.while_1
# import controle.outros_exemplos

# duas formas de chamar a mesma função:
# from funcoes import basico
# basico.saudacao()
# from funcoes.basico import saudacao, saudacao_manha, soma_e_mult
# nome = input("Diga um nome: ")
# saudacao(nome)
# idade = 18
# saudacao_manha(nome, idade)
# saudacao_manha()
# a = soma_e_mult(a=2, c=3)  # passando assim posso pular um valor haha
# b = soma_e_mult(a=3, b=4, c=3)
# print(a + b)

# from funcoes import args
# s = args.soma(1, 2, 7, 8, 9, 10)
# print(s)
# resultado = args.resultado_final(nome = 'Marcos', nota = 5)
# print(resultado)

# from funcoes import funcional
# from funcoes import map_reduce
from funcoes import lambdas_filter


