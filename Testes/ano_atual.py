# Para descobrir o ano atual
import datetime

'''
ano = date.today().year
mes = date.today().month
dia = date.today().day
'''
agora = datetime.datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M:%S")) # Reorganiza a posição da data e exibe horas 