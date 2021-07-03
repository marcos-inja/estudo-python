def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total


def resultado_final(**kwargs):
    elogio = f'Párabens {kwargs["nome"]} você passou' if kwargs['nota'] >= 6 else 'você ficou' 

    return f"{elogio} com a nota {kwargs['nota']}"