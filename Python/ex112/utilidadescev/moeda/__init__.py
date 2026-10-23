def metade(p, formt=False):
    '''
    p --> é o preço

    formt -> se for True retorna o valor formatado

    retorna a metade de p
    '''
    if formt:
        return moeda(p/2)
    else:
     return p/2

def dobro(p, formt=False):
    '''
    p --> E o valor do preço
    formt -> se for True retorna o valor formatado
    retorna o dobro de p
    '''

    if formt:
        return moeda(p*2)
    else:
        return p * 2

def aumentar(p, taxa, formt=False):
    '''
    Aumenta o valor de p de acordo com a taxa (que esta em porcentagem)
    p --> valor do preço
    taxa --> valor em porcentagem
    formt -> se for True retorna o valor formatado
    '''
    taxa_aplicada = (p * taxa) / 100 # Descobre quanto é  a taxa sobre o preço base
    p = taxa_aplicada + p # Atualiza o preço base para o preço + a taxa

    if formt:
        return moeda(p)
    else:
        return p

def diminuir(p, taxa, formt=False):
    '''
    Diminui o valor de p de acordo com a taxa (que esta em porcentagem)
    p --> valor do preço
    taxa --> valor em porcentagem
    formt -> se for True retorna o valor formatado
    '''
    taxa_aplicada = (p* taxa) / 100 # Descobre quanto é  a taxa sobre o preço base
    p = p - taxa_aplicada # Atualiza o preço base, para preço - taxa

    if formt:
        return moeda(p)
    else:
     return p

def moeda(p):
    '''
    Formata a moeda para aparcer com R$ e virgula no lugar do ponto
    '''
    return f'R${p:.2f}'.replace('.', ',')

def resumo(p=0, aum=10, reduz=5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR"}'.center(30))
    print('-'*30)

    print(f'Preço Analisado: \t {moeda(p)}')
    print(f'Dobro do Preço: \t {dobro(p, True)}')
    print(f'Metade do Preço: \t {metade(p, True)}')
    print(f'{aum}% de Aumento: \t {aumentar(p, aum, True)}')
    print(f'{reduz}% de Redução: \t {diminuir(p, reduz, True)}')
    print('-'*30)