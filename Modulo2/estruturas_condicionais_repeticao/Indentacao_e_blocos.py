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

def sacar():
    if not verificar_senha():
        return "Acesso negado, senha incorreta."
    
    saldo = 500
    print(f"Seu saldo é: {saldo}")
    saque_inicial = int(input("Digite o valor do seu saque: "))
    
    if saldo >= saque_inicial:
        saldo -= saque_inicial
        return f"Saque realizado com sucesso. Saldo restante: {saldo}"
    else:
        return "O saque não foi realizado, saldo insuficiente"

# Chamada da função sacar
print(sacar())
