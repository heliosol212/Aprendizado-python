#
#Identação:
#A identação ajuda a deixar o código mais legível e manutenível, além de ajudar o interpretador
#a saber aonde o bloco do código começa. 

#Bloco de comando:
#As linguagens geralmente costumam usar comandos para iniciar e finalizar blocos de código

#por exemplo(Em php):
#if {
#};

#as chaves '{}' são caracteres que funcionam como comandos para iniciar '{' e fechar o bloco '}'.

#Em python, é importante (por incentivo) a cada bloco de código dar uma espaço de 4 linhas

#Exemplo:


#a = 2
#b = 3
#def qlqcoisa():
    #if(a >= b or b >= a):
    #return("qlqcoisa")

    #Fim do bloco if

#Fim do bloco def(funcao)

#Exemplo de codigo com identacao e blocos:


senha_correta = "senhafoda"

def verificar_senha():
    while True:
        senha = input("Digite sua senha: ")
        if senha == senha_correta:
            return True
        else:
            print("Senha incorreta. Tente novamente.")

def deseja_outra_operacao():
    while True:
        resposta = input("Deseja realizar outra operação? (S/N): ").strip().upper()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            return False
        else:
            print("Resposta inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")

def saldo_insuficiente():
    print("O saque não foi realizado, saldo insuficiente.")

def sacar():
    if not verificar_senha():
        return "Acesso negado, senha incorreta."
    
    saldo = 500
    print(f"Seu saldo é: {saldo}")
    saque_inicial = int(input("Digite o valor do seu saque: "))
    
    if saldo >= saque_inicial:
        saldo -= saque_inicial
        print(f"Saque realizado com sucesso. Saldo restante: {saldo}")
    else:
        saldo_insuficiente()

    if deseja_outra_operacao():
        sacar()
    else:
        return "Operação finalizada."

# Chamada da função sacar
print(sacar())

#Nota: Para chamar uma variável para dentro de uma string, use a funçao 'f' antes de qualquer string
#Exemplo:

#c = "sexoo"
#print(f"a variavel 'c' tem esse valor: '{c}'")
