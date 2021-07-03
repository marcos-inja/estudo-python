import time
total = 0
qtde = 0
nota = 0
maior_nota = 0
menor_nota = 100 # Olha a gambiarra kkkk

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair '))

    if nota != -1:
        qtde += 1
        total += nota

        if maior_nota <= nota:
            maior_nota = nota

        if menor_nota >= nota:
            menor_nota = nota


print(f'O total é: {total} \nA média é {total / qtde} \nO total de notas é {qtde} \nA maior nota é {maior_nota} \nA menor nota é {menor_nota}')


z = 10

while z:
    print(z)
    time.sleep(0.4)  #Vai aparecer um numero a cada 0.4s
    z -= 1
