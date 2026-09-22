def metade(p):
    '''
    p --> é o preço

    retorna a metade de p
    '''
    return p/2

def dobro(p):
    '''
    p --> E o valor do preço

    retorna o dobro de p
    '''
    return p * 2

def aumentar(p, taxa):
    '''
    Aumenta o valor de p de acordo com a taxa (que esta em porcentagem)
    p --> valor do preço
    taxa --> valor em porcentagem
    '''
    taxa_aplicada = (p * taxa) / 100 # Descobre quanto é  a taxa sobre o preço base
    p = taxa_aplicada + p # Atualiza o preço base para o preço + a taxa
    return p

def diminuir(p, taxa):
    '''
    Diminui o valor de p de acordo com a taxa (que esta em porcentagem)
    p --> valor do preço
    taxa --> valor em porcentagem
    '''
    taxa_aplicada = (p* taxa) / 100 # Descobre quanto é  a taxa sobre o preço base
    p = p - taxa_aplicada # Atualiza o preço base, para preço - taxa
    return p
