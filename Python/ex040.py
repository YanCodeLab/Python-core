#Media de notas
from time import sleep # Importa comando delay
print(30*'=-') # Linha
print('CALCULADORA DE NOTAS') # Titulo
print(30*'=-') # Linha
sleep(1)
n1 = float(input("Digite á Primeira nota: ")) # Recebe nota 1
print(30*'=-') # Linha
sleep(1)
n2 = float(input("Digite a Segunda nota :")) # Recebe nota 2
print(30*'=-') # Linha
sleep(2)
print('Calculando...') # Mensagem de Carregamento
sleep(2)
print(30*'=-') # Linha
media = (n1 + n2) / 2 # Calcula media aritmetica das notas
if n1 > 10 or n2 > 10: # Caso usuario coloque uma nota acima de 10
    print('Valor Invalido') # Mensage de erro
    sleep(1)
    print('Suas notas deve ser de 0 a 10') # Sugere correção
elif media < 5: # Se a media for menor que 5
    print('Reprovado') #status de aprovação
    print(f'Sua media é {media}') # Exibe media
elif media >= 7: # Se media for maior que 7
    print('Aprovado') # Status
    print(f'Sua media é {media}') # Exibe media
else: # Se não(media entre 5 e 6)
    print('Fará Recuperação')# Status
    print(f'Sua media é {media}') # Exibe media
