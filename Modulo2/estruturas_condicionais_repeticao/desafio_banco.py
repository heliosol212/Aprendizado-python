#Deposito
saldo = 1000
print("<--Deposito-->")

def deposito():
    valor_deposito = int(input("Digite o valor do depósito: "))
    saldo += valor_deposito  # Adiciona o valor_deposito ao saldo atual
    return saldo  # Retorna o saldo atualizado
    
novo_saldo_apos_deposito = deposito()
print(deposito())

print(f"seu saldo após o deposito é de {novo_saldo_apos_deposito}")

print("<--Saque-->")

def saque():
    saque = int(input(""))
    saldo -= saldo
    return saldo
print(saque())

novo_saldo_apos_saque = saque()
print(f"seu saldo após o saque é de: {saldo}")
    