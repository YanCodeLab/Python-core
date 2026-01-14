# Códigos ANSI para cores e formatação de texto
cor = {
    'reset': '\033[0m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',

    # Cores de texto
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',

    # Cores de fundo
    'fundo_preto': '\033[40m',
    'fundo_vermelho': '\033[41m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
    'fundo_azul': '\033[44m',
    'fundo_roxo': '\033[45m',
    'fundo_ciano': '\033[46m',
    'fundo_branco': '\033[47m',
}

print(40*f'{cor["roxo"]}=-{cor["reset"]}')                                                         #Linha decorativa