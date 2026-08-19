lista = []
while True: # Laço infinito
    lista.append(int(input('Digite um Valor: '))) # Adiciona um valor na lista
    end = str(input('Deseja Continuar [S/N]: ')).upper() # Recebe se o usuario deseja continuar
    if end == 'N': # Se usuario escolher N
        break # Interrompe o laço

print(f'Voce digitou {len(lista)} elementos') # Exibe quantas vezes digitou 
lista.sort(reverse=True)
print(f'Os numeros que voce digitou em forma ordenada são: {lista}') # Exibe usando sort
presente = None # Define como vazio a variavel que salva a presença do numero 5 
for pos, c in enumerate(lista): # percorrre a lista
        if c == 5: # Se encontar o numero 5 
             presente = True # Define presença como verdadeiira
             posição = pos # Salva a posição onde o 5 se encontra

if presente == True: # Se a presença de 5 for verdadeira
    print(f'O numero 5 faz parte na lista, na posição {pos}')
else: # Se for falsa
     print('O numero 5 não faz parte da lista')