produtos = ("Arroz", 29.90,
          "Feijão", 8.99, 
          "Leite", 5.49, 
          "Óleo de Soja", 7.89, 
          "Açúcar", 4, 
          "Café", 18.90, 
          "Macarrão", 4.29, 
          "Sabão em Pó", 16.50)

print(40*'-')
print('LISTAGEM DE PREÇOS')
print(40*'-')
for pos in range(0, len(produtos)):# pos vira o numero das posiçoes dos itens
    if pos % 2 == 0: # Sabemos que todo item que esta em uma posição par e produto
        print(f'{produtos[pos]:.<30}', end='')
    else: # E todo item que esta na posição impar e preço
        print(f'{produtos[pos]:>.2f}')
print(40*'-')