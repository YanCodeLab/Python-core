def voto(ano):
    """
    Função que calcula a idade e analisa se pode votar ou não
    
    ano = ano de nascimento 

    pode retornar 3 mensagens
    -> NÃO VOTA (Para menores de 16 anos)
    -> VOTO OBRIGATORIO (De 16 anos ate 64 anos)
    -> VOTO OPCIONAL ( De 65 anos para cima)
    """
    from datetime import date

    idade =  date.today().year - ano

    if idade < 16:
        return f'Com idade {idade} anos: NÃO VOTA'

    if idade >= 16 and idade < 65:
         return f'Com idade {idade} anos: VOTO OBRIGATORIO '

    if idade >= 65:
         return f'Com idade {idade} anos: VOTO OPCIONAL '


# programa principal
print('-'*30)
nasceu = int(input('Digite o Ano em que voce nasceu: '))
print(voto(nasceu))
print('-'*30)
