def formata (txt): # Formata para que as linhas sejam adptaveis
    tamanho = len(txt) + 4 #Define que o tamnaho sera igual a qtd de letas da frasde (o + 4 serve somete para ter uma borda)
    print('~' * tamanho ) # Linha sera do tamanho da palavra
    print(f'  {txt}') #frase cpm espaço para centralizar
    print('~' * tamanho) # # Linha sera do tamanho da palavra


formata('LINHAS ADAPTAVEIS') # Titulo com linhas adptaveis

while True: 
    titulo = str(input('Digite uma frase ou palavra: '))# Recebe palavra 
    formata(titulo) # Formata pa que seja exibido com linhas adptaveis

    #loop continua?
    continua = str(input('Deseja testar novamente [S/N]')).upper() # Continua programa?
    print('-'*30) # linha
    if continua in 'N': # Se for N
        break# Encerra loop

formata('VOLTE SEMPRE :)') # Encerra Programa
