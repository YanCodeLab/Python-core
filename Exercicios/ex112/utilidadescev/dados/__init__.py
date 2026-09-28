def leiaDinheiro(d):
    valido = False # Variavel de controle
    while not valido: # ebquanto não for valido
        din = str(input(d)).replace(',','.').strip()# recebe o valor em string, substiui a virgula por ponto e apaga os espaços inuteis

        if din.isalpha() or din == '': #Se o valor recebido for do tipo alphanumerico (alfanumérico é aquele que contém letras e/ou números.) ou  se estiver vazio
            print(f'\033[31mERRO: O valor "{din}" não é valido!\033[0m') # Da erro
        else:# Se não
            valido == True # O valor e considerado valido
            return float(din)# retona o valor em float
        

