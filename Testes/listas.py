#Listas


# ==================== COMANDOS PRINCIPAIS PARA USAR EM LISTAS ====================
#
# append(valor)
#     → Adiciona um novo valor ao final da lista.
#
# insert(posição, valor)
#     → Adiciona um valor em uma posição específica da lista.
#
# remove(valor)
#     → Remove a primeira ocorrência desse valor na lista.
#
# pop()
#     → Remove e retorna o último valor da lista. (pop(i) remove pelo índice)
#
# clear()
#     → Limpa a lista inteira, deixando ela vazia.
#
# sort()
#     → Ordena a lista em ordem crescente. (sort(reverse=True) para decrescente)
#
# len(lista)
#     → Retorna a quantidade de itens dentro da lista.
#
# sum(lista)
#     → Soma todos os valores numéricos da lista (apenas int ou float).
#
# max(lista)
#     → Retorna o maior valor da lista.
#
# min(lista)
#     → Retorna o menor valor da lista.
#
# in
#     → Verifica se um valor está dentro da lista. Ex: if x in lista:
#
# join()
#     → Junta os itens da lista em uma string (somente se forem strings).
#        Ex: ", ".join(lista)  # Exibe: item1, item2, item3
#
# ================================================================================




from random  import choice # Importa comando para sorteio aleatorio
from time import sleep # Comando para delay
print('-=' * 40) # Linha
print('Treinado Listas') # Titulo
print('-=' * 40)# Linha
lista = ['maça', 'banana', 'laranja'] # Lista criada

print('Veja algumas frutas: maça banana laranja ')# exibe itens da lista
print('-' * 40)# Linha

qtd = int(input('Digite Quantas novas frutas vc quer adicionar na lista:')) # Recebe a quantidade de quantas novas frutas sera adicionada na lista
if qtd > 0: # Se a quantidade for maior que 0
    for c in range (1, qtd+1): # Ira repertir a pergunta de acordo com a quantidade de novas frutas
        fruta = str(input('Digite a nova fruta:')) # Recebeo nome da nova fruta
        if fruta in lista: # Se a nova fruta ja estiver na lista
            print('A fruta ja esta na lista') # Aviso de repetição
        else:    # Se a nova fruta não estiver na lista
             lista.append(fruta) # Adiciona nova fruta na lista
             print('Fruta Salva na Lista')# aviso de confirmação
             print('-' * 40)# Linha
    exibir = ", ".join(lista) # Este comando serve para formatar a lista (Evita que apareça aspas e virgula)
    sleep(2)# Delay
    print(f'Veja a seguir todas as frutas salvas\n{exibir}')# Exibi todas as frutas da lista
    sleep(2)# Delay
    print('-=' * 40)# Linha
    
# Segunda função do programa 
    print('ESCOLHENDO UM ITEM DA LISTA') # Titulo
    print('-=' * 40)# Linha
    escolhida = choice(lista) # Escolhe uma fruta aleatoria dentro da lista
    print('Vou escolher uma dessas frutas...')# aviso de espera
    sleep(1)# Delay
    print(f'Eu escolho {escolhida}')# Exibi fruta escolhida
    print('-' * 40)# Linha
    sleep(3)# Delay
else: # Se não (Caso ele nao queira adicionar novas frutas na lista, ou colocou valor invalido)
    print('Valor invalido')# Mnesagem de erro


# -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -=
# Revisão geral
# -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -=

# Aqui foi utilizado o comando .append() para adicionar um novo valor
# a uma lista já existente.

# ------------------------------------------------------------------------------------

# Comando join:
# O join serve para formatar os resultados dentro de uma lista e exibi-los
# como texto contínuo, sem aspas e sem colchetes.

# ------------------------------------------------------------------------------------

# Observação importante:
# Se a lista contiver números e você quiser exibi-los usando join,
# é necessário converter cada número para string.
#
# Exemplo:
# numeros = [1, 2, 3]
# resultado = ", ".join(str(n) for n in numeros)
# # O for acima serve para converter todos os itens da lista em string.
# # Resultado mostrado: 1, 2, 3

# ------------------------------------------------------------------------------------

# Como usar join com apenas 1 número:
# Para usar join, você precisa passar uma lista de strings.
# Se tiver apenas um número, transforme-o em lista primeiro.
#
# Exemplo:
# numero = 5
# resultado = ", ".join([str(numero)])
# # Isso exibe: 5

# -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -=

