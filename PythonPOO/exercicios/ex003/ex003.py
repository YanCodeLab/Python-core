class ContaBancaria:

    ''''
    Cria uma conta bancaria que permite fazer saques e depositos
    '''

    def __init__(self, id, nome, saldo=0): # Metodo contrutor
        # Atributos
        self.id= id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta Criada Com Sucesso -  Saldo: R${self.saldo:,.2f}')
        print('-' * 60)

    #Metodos
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem o saldo R${self.saldo:,.2f}'


    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}')
        print('-' * 60)

    def sacar(self, valor):
        if valor <= self.saldo: # Se o valor de saque for menor ou igual ao valor que tem na conta
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} Autorizado da conta {self.id}')
        else: # Se caso o valor do saque supere o saldo na contad
            print(f'Saque Não Autorizado, R${valor:,.2f} supera o saldo total da conta {self.id} ')
        print('-' * 60)

c1 = ContaBancaria(132, 'Yan', 3000)

c1.depositar(500) # Deposita 500 reais
c1.sacar(15000)    #Retira 1500 reais do saldo
print(c1)
print('-' * 60)