times = (  # TABELA DO BRASILEIRÃO 2026
    "Palmeiras",
    "Flamengo",
    "Fluminense",
    "São Paulo",
    "Athletico-PR",
    "Bahia",
    "Bragantino",
    "Vasco",
    "Coritiba",
    "Vitória",
    "Cruzeiro",
    "Botafogo",
    "Atlético-MG",
    "Internacional",
    "Santos",
    "Corinthians",
    "Grêmio",
    "Mirassol",
    "Remo",
    "Chapecoense"
)
print('=-'*80)
print(f'Lista de Times do Brasileirão: {times}') # Exibir todos os times 
print('=-'*80)
print(f'Os 5 primeiros times são: {times[0:5]}') # Exibi os primeiros 5 colocados
print('=-'*80)
print(f'Os 4 ultimos são: {times[-4:]}') # Exibi os 4 ultimos colocados
print('=-'*80)
print(f'Times em ordem alfabética: {sorted(times)}') # Exibi todos em ordem alfabetica
print('=-'*80)
print(f'A Chapecoense está na {times.index('Chapecoense') + 1}° posição')  # Exibi a posição do time da chapecoense (+ 1 pois o primeiro colocado esta na posiçao  0)