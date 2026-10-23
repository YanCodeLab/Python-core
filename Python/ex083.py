'''

A ideia é: 

Quando encontra ( → coloca na pilha.
Quando encontra ) → tenta remover um ( da pilha.
Se não houver ( para remover, a expressão já está errada.

No final:

Se a pilha estiver vazia → todos os parênteses foram fechados corretamente.
Se sobrar algo na pilha → faltou fechar algum parêntese.

'''
expres = str(input('Digite uma expressão: ')) 
pilha = []
for simb in expres:
    if simb == '(': 
        pilha.append('(')
    if simb == ')':
        if len(pilha) > 0:
            pilha.pop() # apaga o ultimo elemento de uma lista 
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\033[32mA expressão esta valida\033[0m')

else:
     print('\033[31mA expressão esta incorrreta\033[0m')
