# Este codigo faz a função do comando sort
lista = list()
for p in range(0, 5):
    num = int(input('Digite um Numero: ')) # Recebe o numero
    if p == 0 or num > lista[-1]: # Se for o primeiro valor ou o maior valor 
     lista.append(num) #Adiciona o numero ao final da lista 
     print('Adicionado ao final da lista')
    else:
       posição = 0 # contador de posição para lermos a lista
       while posição < len(lista):# enquanto a posição for menor que a quantidade de itens na lista
          if num <= lista[posição]: # Se o numero digitado for menor que o valor atual na osição da lista
             lista.insert(posição, num) #inseri o numero 
             print(f'Adicionado na posição {posição} da lista')
             break # encerra o laço 
          posição +=1 # passa para o proximo item da lista
print(lista)