from rich.traceback import install
install() # Monitora para se caso der erro

# Codigo abaixo ira tr um erro proposital

def divi(x,y):
    return x/y

c = divi(10,0)
print(c)

# Perceba que a mensagem de erro sera formatada pelo install()