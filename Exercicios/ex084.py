pessoas = []
dado = []
maior_peso = menor_peso = 0 
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior_peso = menor_peso = dado[1] # Define o primeiro valor digitado como menor

    else: # Compara os novos valores com os anteriores
        if dado[1] > maior_peso: # Se o dado digitado agora for maior que o o maior peso
            maior_peso = dado[1] # atualiza o valor do maior peso para esse dado
        if dado[1] < menor_peso:# Se o dado digitado agora for menor que o o menor peso
            menor_peso = dado[1]# atualiza o valor do menor peso para esse dado

    pessoas.append(dado[:]) # Salva o dado na lista principal
    dado.clear()# Limpa os dados atuaias

    continuar = str(input('Deseja Continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(f'Ao todo voce cadastrou {len(pessoas)} pessoas.')


print(f'O maior peso é {maior_peso} ', end='')

for p in pessoas:
    if p[1] == maior_peso:
        print(f'({p[0]})', end='')
        print()


print(f'O menor peso é {menor_peso}', end='')

for P in pessoas:
    if P[1] == menor_peso:
        print(f'({P[0]})', end='')
        print()
