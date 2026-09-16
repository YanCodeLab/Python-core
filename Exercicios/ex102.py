def fatorial(n, show=False): 
    '''
    Calcula o Fatorial de um Numero 

    --> para n : Numero a ser calculado
    --> para show: (opcional) mostrar ou não a conta
    --> return: O Fatorial de n
    
    '''
    cont = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ',end='')

        cont *= c # Calcula o resultado do fatorial
    return cont

print(fatorial(5, show=True)) # Se show=True ele mostra a conta se não tiver show ou for show=False ele so mostra o resultado
help(fatorial)