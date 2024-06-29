#Desafio do banco

#Deposito
saldo = 500
saque_max = 3  

while True:
    print("\n[1] Depósito [2] Saque [3] Extrato [4] Sair")
    escolha = int(input("Digite qual operação deseja realizar: "))

    if escolha == 1:  # Depósito
        deposito = int(input("Digite o valor do depósito: "))
        saldo += deposito
        print(f"Depósito realizado com sucesso. Seu saldo atual é: {saldo}")
    
    elif escolha == 2:  # Saque
        while saque_max > 0:
            saque = int(input("Digite o valor do seu saque: "))
            if saque > saldo:
                print(f"Saldo insuficiente. Seu saldo atual é {saldo}")
            else:
                saldo -= saque
                saque_max -= 1
                print(f"Saque realizado com sucesso. Seu saldo atual é: {saldo}")
                print(f"Você tem {saque_max} saques restantes para hoje.")
            
            if saque_max > 0:
                continuar = input("Deseja realizar outra operação de saque? (S/N): ").strip().upper()
                if continuar != "S":
                    break

        if saque_max == 0:
            print("Você não tem mais saques restantes para hoje. Tente novamente amanhã.")
    
    elif escolha == 3:
        print(f"Seu extrato é: {saldo}")
        

    elif escolha == 4:
        print("Encerrando operações...")
        break
        
    
    else:
        print("Opção inválida. Tente novamente.")

print(f"\nOperação finalizada. Seu saldo final é: {saldo}.")

    


    















    