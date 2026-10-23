print('='*50)
print(f'BANCO RANGEL')
print('='*50)
valor = int(input('Qual valor voce quer sacar? R$')) # Recebe valor
total = valor
ced = 50 # Valor da cedula
totced = 0 # Conta quantas notas são necessarias
while True: # loop infinito
    if total >= ced: # se o total for maior ou igual a cedula atual
        total -= ced # Subtrai o valor da cedula do total
        totced += 1 # adiciona 1 parav copntar a qtd de cedulas
    else: # Se não (caso o total seja menor que o valor de cedula)
        if totced > 0: # para exibir somente oq tiver cedula
            print(f'Total de {totced} cedulas de R${ced}') # exibi informaçoes
        if ced == 50: # Se a cedula for igual a 50
            ced = 20 # Transforma em 20
        if ced == 20: # Se a cedula for igual a 20
            ced = 10 # Transforma em 10
        if ced == 10: # Se a cedula for igual a 10
            ced = 1 # Transforma em 1
        totced = 0 # Apos trasforma a cedula em outra reinicia a contagem
        if total == 0: # Se o total chegar a 0
            break # Encerra o loop
print('Volte sempre')
