pessoas = [] # Armazena todos os usuarios 
user = {} # Recebe o usuario temporariamente

while True:
    print('-'*30)
    user['nome'] = str(input('Nome: ')) #Recebe nome

    
    #---------------------------------Validação de sexo -------------------------------------------------
    while True:
     user['sexo'] = str(input('Sexo [M/F]: ')).upper() [0] # Recebe sexo e pega so a primeira letra
     if user['sexo'] in  'MF': # Se caso o valor recebido  seja M ou F
        break
     print('ERRO: Digite apenas M ou F') #Mensagem de erro
            
    #-----------------------------------------------------------------------------------------------------
    
    user['idade'] = int(input('Idade: ')) # Recebe Idade 

    pessoas.append(user.copy()) #Salva os dados do usuario na lista pessoas
    

    add_user = str(input('Deseja adicionar mais uma pessoa? [S/N]: ')).upper() # Variavcel de confirmação para se deseja dicionar mais uma peoa ou encerrar
    #------------------------Validação add_user -------------------------------------
    if add_user not in 'SN':
        while add_user not in 'SN':
            print('ERRO: Digite apenas S ou N')
            add_user = str(input('Deseja adicionar mais uma pessoa? [S/N]: ')).upper()
    #--------------------------------------------------------------------------------

    if add_user in 'N':
        break

print('-'*30)
# ANALISANO OSA DADOS COLETADOS
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas') # Total de pessoas cadastradas

print('-'*30)

soma_idades = 0 # Contador para somar as idades 
for i in pessoas: # v percorre a lista pessoas
   soma_idades += i['idade'] # soma as idades
   media_idades = float( soma_idades / len(pessoas) ) # faz a media de idade de todos
print(f'B) A media das idades é {media_idades}') # Exibe a media

print('-'*30)

print('C) As mulheres cadstradas foram ',end='')
for m in pessoas: # pERCORRE A LISTA PESSOAS
    if m['sexo'] in 'F': # Se encontar sexo Feminino
     print(f"{m['nome']}  ", end='') # Exibe o nome das mulheres cadastradas
print()
    
print('-'*30)

print('D) A lista das pessoas que estão com a idade acima da media são: ')
for acima in pessoas: # Percorrer a lista
    if acima['idade'] >= media_idades: # Se alguma idade for maior que a media de idades 
        print('') 
        for k,v in acima.items():
           print(f'{k} = {v}: ', end='') # Exibe ficha do usuario
print()
print('<<ENCERRADO>>')  #Fim
