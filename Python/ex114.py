import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/') # ACESSA O SITE

except urllib.error.URLError:
    print('O site do youtube não esta acessivel no momento!')

else:
    print('Consegui acessar o youtube do pudim com sucesso')