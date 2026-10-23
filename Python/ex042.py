#REVISAR

#Analisando triangulos
#Formando Triangulos
print(20*'=-')
print('Analisando Triangulos')
print(20*'=-')
r1 =  float(input('Digite o Valor de um segmento:'))
r2 =  float(input('Digite o Valor de um segmento:'))
r3 =  float(input('Digite o Valor de um segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
   print('Os segmentos acima podem formar um triangulo')
   if r1 == r2 == r3:
    print('Os segmentos formaram um triangulo EQUILATERO, com todos os lados iguais')

   elif r1 != r2 != r3 != r1:
    print('Os segmentos formaram um triangulo ESCALENO')

   else:
    print('Os segmentos formaram um triangulo ISOCELES')
 
else:
    print('Os Segmentos acima não podem formar um triangulo')

