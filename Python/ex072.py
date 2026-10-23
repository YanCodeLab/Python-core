extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'  ) #Tupla

num = int(input('Digite um Numero de 0 á 20: '))
while True:
    
    if num < 0 or num > 20:
        num = int(input('Tente Novamente. Digite um Numero Entre 0 e 20: ')) 
    else:
        print(f'Voce Digitou o numero {extenso[num]}')
        break

