#Tabuada v3.0
while True: #Loop infinito
    print('-'*50)#Linha
    n = int(input('Quer ver a tabuada de qual valor: ')) #Recebe o numero
    if n < 0: # Se n for menor que 0
       break #Interrompa o programa
    for c in range(1,11): # Repete 10 vezes
     print(f'{n} x {c} = {n*c}') #Exibi linha da tabuada 
print('-'*50)#Linha
print('Programa encerrado')#Mensagem final