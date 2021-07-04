def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


# Estou atribuindo a função a váriavel
somar = soma


def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)


# Uso a váriavel somar para que tem uma função dentro dela,
# mas também poderia ter usado a função
resultado = operacao_aritmetica(somar, 3, 4)
print(resultado)

# Aqui passo a função diretamente sem coloca-lá em uma váriavel
resultado = operacao_aritmetica(sub, 3, 4)
print(resultado)


# Usado caso tenha um processamento bem alto
def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma


# Duas formas de fazer o mesmo
# Como o retorno vai ser uma função, posso invocar assim
resultado_final = soma_parcial(10)(12)
print(resultado_final)

# Ou dessa outra forma para ficar mais fácil de "entender" kk
# A váriavel fn recebe a função concluir soma com o return assim: 10 + b
fn = soma_parcial(10)
# Aqui vai ser adicionado 12 na váriavel b do return
resultado_final = fn(12)
print(resultado_final)
