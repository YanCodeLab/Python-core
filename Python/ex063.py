# Sequencia de Fibonacci
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos voce quer mostrar:  ')) # Recebe quantos termos serão mostrados na sequencia
t1 = 0 # O primeiro termo sempre é 0
t2 = 1 # O segundo termo sempre é 1
print(f'{t1} -> {t2}', end = '-> ') # Exibi
cont = 3 # Contador de termos, ja esta com tres pois ja temos os primeiros 3 termos 
while cont <= n: # Enquanto o contador não chegar no numero solicitado de termos
    t3 = t1 + t2 # O proximo termo e a soma dos dois anteriores
    print(t3, end='-> ') # Exibir
   # Abaixo redefinimos os termos para 'atualizarem', assim eles sempre serão os antecesores de t3
    t1 = t2 
    t2 = t3
    cont += 1 #adiciona 1 no contador 
print('\nFimm')