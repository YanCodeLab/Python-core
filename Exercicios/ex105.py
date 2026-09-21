def notas(*n, sit=None):
    
    '''
    Analisa uma quantidade de notas e retorna um dicionário contendo o total, maior nota, menor nota e média. 
    Se sit=True, também informa a situação do aluno de acordo com a média.
    
    '''

    #Analise das notas
    boletim = {} # Cria o dicionario boletim

    boletim['total'] = len(n) # Total de notas 

    boletim['maior'] = max(n)

    boletim['menor'] = min(n)

    boletim['media'] = sum(n) / len(n)

    if sit == True:
        if boletim['media'] <= 4:
            boletim['situação'] = 'RUIM'

        if boletim['media'] > 4 and boletim['media'] <= 7: 
            boletim['situação'] = 'RAZOAVEL'

        if boletim['media'] > 7 and boletim['media'] <= 10:
            boletim['situação'] = 'BOA' 


    return boletim


#programa pincipal
resp = notas(4, 8, sit=True)
print(resp)