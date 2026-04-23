from random import randint

class Agencia:
    
    def __init__(self,telefone,cnpj,numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0 
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do recomendado. Valor atual: R${self.caixa:.2f}')
        else:
            print(f"OK! Caixa atual: R${self.caixa:.2f}")

    def emprestar_dinheiro(self,valor,cpf,juros):
        if self.caixa > valor:
            self.caixa-=valor
            self.emprestimos.append((valor,cpf,juros))
        else:
            print("Não é possível realizar empréstimo.")

    def adicionar_cliente(self,nome,cpf,patrimonio):
        self.clientes.append((nome,cpf,patrimonio))


#################################
class AgenciaVirtual(Agencia):
    def __init__(self,site,telefone,cnpj):
        self.site = site
        super().__init__(telefone,cnpj,1000)
        self.caixa = 1000000

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        nun_agencia = randint(1000,9999)
        super().__init__(telefone, cnpj, numero=nun_agencia)
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        nun_agencia = randint(1000,9999)
        super().__init__(telefone, cnpj, numero=nun_agencia)
        self.caixa = 10000000

    def adicionar_cliente(self,nome,cpf,patrimonio):
        if patrimonio>=1000000:

            super().adicionar_cliente((nome,cpf,patrimonio))
        else:
            print("Cliente sem o perfil adequado")


print()
print("virtual")
agenciaVirtual_teste = AgenciaVirtual('www.bancovirtual.com',30201010,"778899/0001")
agenciaVirtual_teste.verificar_caixa()
print(agenciaVirtual_teste.__dict__)
print("comum")
agencia_comum_teste = AgenciaComum("20303020","9988776/0001")
agencia_comum_teste.verificar_caixa()
print(agencia_comum_teste.__dict__)
print("premium")
agencia_premium_teste = AgenciaPremium("30405060","1234567/0001")
agencia_premium_teste.verificar_caixa()
print(agencia_premium_teste.__dict__)