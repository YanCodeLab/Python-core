def titulo(txt): # FUNÇÃO PARA FORMATAÇÃO DO TITULO
    print('-'*30)
    print(txt)
    print('-'*30)


def area(l, c): # Função para calcula e exibir a area
    area = l * c # area l=largura e c=comprimento
    print(f'A aréa de um terreno {l}x{c} é igual a {area}m²')

# Programa principal
titulo('  CONTROLE DE TERRENOS  ') # Chama a formatação do titulo
largura = float(input('LARGURA (m): ')) # Recebe valor da largura do terreno
comprimento = float(input('COMPRMENTO (m): ')) # Recebe o valor do comprimento do terreno
area(largura, comprimento) # Chama a função area comos parametros