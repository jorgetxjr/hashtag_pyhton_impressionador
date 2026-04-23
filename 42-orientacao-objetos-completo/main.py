import ContasBancos

###Programa
conta_jorge = ContasBancos.ContaCorrente("Jorge","123.456.789-11",20304050,10101)
conta_mamae = ContasBancos.ContaCorrente("Ivone", "987.654.321-00",20304050,12345)

# print(conta_jorge.nome,conta_jorge.cpf)
# print(conta_mamae.nome,conta_mamae.agencia,conta_mamae.numero_Conta)
# conta_jorge.consultar_saldo()
# conta_jorge.depositar(1000)
# conta_jorge.consultar_saldo()
# conta_jorge.sacar_dinheiro(250)
# conta_jorge.consultar_saldo()
# conta_jorge.transferir(500,conta_destino=conta_mamae)
# conta_mamae.consultar_saldo()
# print("Histórico Jorge:")
# print("*"*25)
# conta_jorge.visualizar_historico_transacoes()
# print()
# print("Histórico Mamãe:")
# print("*"*25)
# conta_mamae.visualizar_historico_transacoes()

# help(ContaCorrente)

cartao_jorge = ContasBancos.CartaoCredito("Jorge Junior", conta_corrente=conta_jorge)
print()
# print(cartao_jorge.__dict__)
cartao_jorge.senha = "9910"
print(cartao_jorge.senha)