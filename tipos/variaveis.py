a = 3
b = 4.5

print(a + b)

texto = 'Sua idade é...'
idade = 28

# dois jeitos de fazer a mesma coisa
print(texto + str(idade)) # converte o numero em string para para juntar
print(f'{texto} {idade}') # é usado para interpolar valores o template alguma do JS

saudacao = 'bom dia'
print(4 * saudacao)

PI = 3.14
raio = float(input('Informe o raio do circulo: ')) # Usa o float para converter para float kkk
# area = PI * raio * raio # metodo raiz
area = PI * pow(raio,2) # metodo nutella, esse pow é para fazer potencia,
                        # poderia ser qualquer número no lugar do 2 para elevar

# print(type(area)) # Usa type para pegar o tipo de dado
print(f'A Área do circulo é {area}')



