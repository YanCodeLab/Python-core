# Calculando valor de produtos
from time import sleep 
print('============== Lojas Yan ==============')
preço = float(input('Digite o valor do produto R$:'))
print('Formas de pagamento disponiveis')
print('[ A ] A vista (Com dinhero ou cheque)')
print('[ B ] A vista (no Cartão)')
print('[ C ] Em até 2x no cartão')
print('[ D ] Em até 3x ou mais no cartão')
print(20*'=-')
pagamento = str(input('Digite a opção escolhida (A ,B, C, D,):')).upper() # Forma de pagamento
print(20*'=-')
sleep(1)
print('Gerando Nota fiscal...')
sleep(2)
print(20*'=-')
if pagamento == 'A':
    desconto = (preço * 10) / 100 # Descobre 10% 
    valor = preço - desconto # Valor com 10% de Desconto
    print(f'Preço total R${preço}\nDesconto aplicado 10%, R${desconto}\nValor total a ser pago:R${valor}')
elif pagamento == 'B':
    desconto = (preço * 5) / 100 # Descobre 5%
    valor = preço - desconto # Valor com 5% de Desconto
    print(f'Preço total R${preço}\nDesconto aplicado 5%, R${desconto}\nValor total a ser pago:R${valor}')
elif pagamento == 'C':
    print(f'Preço total R${preço}\nDesconto aplicado 0%, R$0,00\nValor total a ser pago:R${preço}')
elif pagamento == 'D':
    parcelas = int(input('Quantas Parcelas?')) # Recebe quantidade de parcelas
    juros = (preço * 20) / 100 # Descobre 20%
    valor = preço +juros  # Soma + 20% de juros 
    print(f'Preço total R${preço}\nJuros de 20%, R${juros}\nValor total a ser pago:R${valor} em {parcelas}x')
else:
    print('Valor invalido\n Digite um valor valido')

print(20*'=-')