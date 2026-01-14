# Gerador de senhas com 8 Caracteres v0.1
'''
Programa feito com intuito de testar minhas habilidades de python nivel iniciante

Gerador de senhas de 8 caracters simples + Verificador de senha

   'Nesta primeira versão o programa esta simples usando conceitos basicos de listas, e seleção aleatoria com o modulo random juntamente
   com condiçoes basicas (if, else), tambem adicionei cores para melhorar a experiencia'

Proximos Upgrades
   - Usuario podera definir quantos caracteres terá a senha
    - Configurar quantas letras numeros ou caracteres especias terão.

    - Criar visual interativo
    - Guardar informaçoes de ja senhas criadas

Criado por Yãn Rangel
14/10/2025
'''


import random                                                                 # Importa Biblioteca random
from time import sleep                                                        #Importa comando Resposavel para colocar um delay, entre as mensagens
print(  30 *'{}={}'.format('\033[1;35m', '\033[m')  )                   #Linha Decorativa
print('{}GERADOR DE SENHAS{}'.format('\033[1;34m','\033[m'))            #Titulo
print(  30 *'{}={}'.format('\033[1;35m', '\033[m')  )                   #Linha Decorativa
sleep(1)                                                                      #Delay de 1 segundo
print('{}Seja-Bem Vindo!{}'.format('\033[1;33m', '\033[m'))             #Boas vindas e encera cor na str
sleep(2)                                                                       #Delay 2 segundos
print('{}Criando sua Senha...{}'.format('\033[1;33m', '\033[m'))         #Mensagem de espera
sleep(4)                                                                       #Delay 4 segundos

alfabeto = list('abcdefghijklmnopqrstuvwxyz')   #Cria uma lista de letras
especiais = list('/!@%$?*()#&')                 #Cria uma Lista de caracteres especiais

n1 = random.randint(0,9)                  #Sorteia um numero de 1 a 9 para n1
n2 = random.randint(1,9)                  #Sorteia um numero de 1 a 9 para n2
n3 = random.choice(alfabeto)                    #Escolhe 1  letra do 'alfabeto' para n3
n4 = random.choice(alfabeto)                    #Escolhe 1  letra do 'alfabeto' para n4
n5 = random.choice(especiais)                   #Escolhe 1  caracter 'especial' do para n5
n6 = random.randint(0,9)                  #Sorteia um numero de 1 a 9 para n6
n7 = random.choice(alfabeto).upper()            #Escolhe 1 letra do 'alfabeto' e transforma ela em Maiuscula para n7
n8 = random.choice(especiais)                   #Escolhe 1  caracter 'especial' do para n8

senha =  [str(n1), str(n2), n3, n4, n5, str(n6), n7, n8]                                                                # Converte numeros para strings, (Para poder usar Join)
senha_final = ''.join(senha)                                                                                            # Junta todas as Strings
print('{}Sua senha foi criada:{}{}{}{}'.format('\033[1;33m','\033[m', '\033[1;34m', senha_final, '\033[m'))       # Exibe senha Criada
sleep(1)                                                                                                                # Delay 1 segundo
print(  30 *'{}={}'.format('\033[1;35m', '\033[m')  )                                                            # Linha decorativa
print('{}Vamos testa?{}'.format('\033[1;34m','\033[m'))                                                                                                   # Inicia Teste de Senha
sleep(1)                                                                                                                # Delay 1 segundo
s = input('{}Digite a senha{}'.format('\033[1;33m','\033[m'))                                                                                             # Recebe Senha
print(  30 *'{}={}'.format('\033[1;35m', '\033[m')  )                                                             # Linha decorativa
sleep(1)                                                                                                                # Delay 1 segundo
if s == senha_final:                                                                                                    # Se a senha recebida for igual a senha criada
    print(30 * '{}={}'.format('\033[1;32m', '\033[m'))                                                            # Linha decorativa
    print('{}ACESSO LIBERADO{}'.format('\033[1;32m', '\033[m'))                                                   # Acesso Liberado
    print(30 * '{}={}'.format('\033[1;32m', '\033[m'))                                                            # Linha decorativa
else:                                                                                                                    # Se não
    print(30 * '{}={}'.format('\033[1;31m', '\033[m'))                                                            # Linha decorativa
    print('{}ACESSO NEGADO{}'.format('\033[1;31m','\033[m'))                                                      # Acesso Negado
    print(30 * '{}={}'.format('\033[1;31m', '\033[m'))                                                            # Linha decorativa

print('{}Fim do Programa,\nEspero que tenha Gostado ;)\nReinicie para Recomeçar'.format('\033[1;36m'))                  # Finaliza Programa e agradece


