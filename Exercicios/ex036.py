# ANALISE DE EMPRESTIMOS
''''
Condiçoes 
  * Emprestimo só é aprovado se caso o valor da parcela não ultrapasse 30% d salario do usuario

'''
from time import sleep                                                          #Importa comando sleep

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
print(f'{cor["negrito"]}{cor["azul"]}ANALISE DE CREDITO{cor["reset"]}')                            #Titulo
print(40*f'{cor["roxo"]}=-{cor["reset"]}') 
sleep(1)
emprestimo = float(input(f'{cor["amarelo"]}Digite o valor do emprestimo desejado:{cor["reset"]}'))                #Recebe valor pretendido para o emprestimo
print(40*f'{cor["roxo"]}=-{cor["reset"]}') 
sleep(2)
salario = float(input(f'{cor["amarelo"]}Digite o valor do seu salario:{cor["reset"]}'))              #Recebe o valor do salario
print(40*f'{cor["roxo"]}=-{cor["reset"]}') 
sleep(2)
anos = int(input(f'{cor["amarelo"]}Digite em quantos anos voce pretende pagar:{cor["reset"]}'))      #Recebe o valor em de anos em que se pretende pagar
sleep(1)
print(f'{cor["roxo"]}Analisando seus dados {cor["reset"]}')
meses = 12 * anos                                                                                    #Converte para ano para meses
parcela = emprestimo / meses                                                                         #Valor das paracelas mensais              
salario = (salario * 30) / 100                                                                       #Atualiza variavel salario para o valor de 30% do salario completo
if parcela > salario: 
    print(40*f'{cor["roxo"]}=-{cor["reset"]}')                                                      #Se o valor da parcela for maior que 30% do salario 
    print(f'{cor["negrito"]}{cor["vermelho"]}EMPRESTIMO NEGADO{cor["reset"]}')                      #Emprestimo negado
    print(40*f'{cor["roxo"]}=-{cor["reset"]}') 
else:                                                                                                #Se não
    print(40*f'{cor["roxo"]}=-{cor["reset"]}') 
    print(f'{cor["negrito"]}{cor["verde"]}EMPRESTIMO APROVADO')                                      # Emprestimo Aprovado
    print(40*f'{cor["roxo"]}=-{cor["reset"]}') 