from ..interface import *

def arquivoExiste(nome):
    try: # Tente ver se o arquivo existe
        a = open(nome, 'rt') # Tenta abrir o arquivo
        a.close() # fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo')
    else:
        a = open(nome, 'wt+')
        a.close()

def verPessoas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO: Ao exibir os dados')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';') #divide uma string em pedaços menores e retorna o resultado como uma lista
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
       a.close()

def cadastrarPessoa(ar, n, i): #Nome do arquivo, nome da pessoa, idade
    try:
        a = open(ar, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('Erro ao adicionar cadastro')