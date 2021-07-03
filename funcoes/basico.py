
def saudacao(nome):
    print(f'Olá {nome}')


def saudacao_manha(nome, idade=20):  # quando usa valores padão você tem várias
    # formas de chamar a mesma função
    print(f'Olá {nome} voce nem parece ter {idade} anos!')


# def saudacao_manha():  # posso sobrescrever as funções
#     print(__name__)

def soma_e_mult(a=0, b=0, c=1):
    return (a + b) * c


# Só é executado se esse for o arquivo main
if __name__ == '__main__':
    saudacao_manha('Marcosss')
