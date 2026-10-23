#Numeros primos
div = 0 # Numeros divisiveis
num = int(input('Digite um Numero: ')) # Recebe numero
for c in range(1, num + 1 ):# Repete de acordo com a variavel num
   if num % c == 0: #Se for divisivel
      print('\033[33m ', end=' ')# o numero fica com a  cor amarela
      div += 1 # adciona 1 na variavel de numeros divisiveis
   else:# se nao
      print('\033[31m ', end=' ')# o numero fica com a  cor vermelha
 
   print(f' {c}', end=' ')# exibe sequencia de numeros
print(f'\n\033[mO numero {num} é divisivel {div} vezes')# exibi informaçoes
if div == 2: # se o 'num' tiver 2 divisores
   print('POR ISSO ELE É CONSIDERADO PRIMO')# numero primo
else:#se nao
      print('POR ISSO ELE NÃO É CONSIDERADO PRIMO')# nao é primo