from funçoes.interface import *
from funçoes.arquivos import *
from time import sleep

arq = 'Pessoas.txt' # Nome do arquivo que contem os cadastros

if not arquivoExiste(arq):
    criarArquivo(arq)
    print(f'Arquivo {arq} foi criado')




while True:
 resultado = menu(['Ver Pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])

 if resultado == 1:
    cabeçalho('Opção 1')
    verPessoas(arq)

 elif resultado == 2:
   cabeçalho('Opção 2')
   nome = str(input('Nome: '))
   idade = leiaInt('Idade: ')
   cadastrarPessoa(arq, nome, idade)
   print(f'Novo registro {nome} foi adicionado')

 elif resultado == 3:
    cabeçalho('Saindo do Sistema, até logo')
    break

 else:
    print('\033[31mErro: Digite uma opção valida\033[0m')
 sleep(2)
