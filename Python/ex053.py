frase = str(input('Digite uma palavra:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1): 
    inverso += junto[letra]
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
print(junto,  inverso)

'''
É POSSIVEL INVERTER A PALAVRA UOU FRASE USANDO APENAS O FATIAMENTO
print(frase[::-1]) 
'''