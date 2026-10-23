def leiaInt(valor):

    '''
    Recebe o parametro valor

    analisa se valor é string ou e numero 

    se for numero retorna o valor como inteiro

    se for string entra em um loop infinito, que so se desfaz quando receber um numero
    '''
    
    num = str(input(valor)) # Le o valor digitado

    while True:
        if num.isnumeric():
            num = int(num)
            return num
            
        else:
            print('\033[31mERRO! Digite um numero inteiro valido!\033[0m')
            num = str(input(valor)) # Le o valor digitado

#programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
