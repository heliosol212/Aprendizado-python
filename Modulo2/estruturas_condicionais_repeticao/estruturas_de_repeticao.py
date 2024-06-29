"""Estruturas de repetição:

São utilizadas para repetir um trecho de um código por um determinado numero de vezes.


"""

#a = int(input(" Digite um numero: "))

#como funciona uma repetição manual:
"""
a += 1
print(a)

a += 1
print(a)

"""

#For: Usado quando há certeza de quantas vezes o bloco deve ser repetido, ou quando queremos repetir um objeto repetivel
#Exemplo:

texto = str(input("Digite um texto"))
VOGAIS = "UOIEA"

for letra in VOGAIS: 
    if letra.upper() in VOGAIS: #Verifica se letra está dentro de vogais
        print(letra, end="")
#else:
    #print() #quebra de linha

        #no "for" é possível usar um else


#Função range():
"""
A função range funciona produzindo uma sequencia de numeros inteiros a partir de um 
inicio(opcional) e um fim(obrigatorio)

Estrutura:

range(inicio, fim, step)

inicio(opcional)
fim(obrigatorio)
step(opcional) --> Intervalo da soma ou subtração de cada numero
"""
#exemplo:

list(range(4))
#retorna: [1, 2 ,3 ,4]

#Com inicio e fim:

list(range(1, 4)) #inicio 1, fim 4
#Retorna: [1, 2, 3]

#Como posso ver, o fim não aparece, apenas é usado como ponto de parada. Ou seja
#Se for inicio 1, e final 4, ele ira executar "1, 2, 3" e 4 é o fim então não é executado.


#For com o range():
for numero in range(0, 11): #ele vai adicionar 1 à "numero" do 0 ao 10.
    print(numero, end="")

#Com step:

for numero in range(0, 51, 5): #conta de 5 em 5. 
    print(numero, end=",")



#While:
"""
Executa um comando até que algo seja verdadeiro/falso;
Pode executar um bloco enquanto um valor for diferente de outro valor.
Também quando não sabemos o numero exato de quantas vezes devem ser repetidas.

"""
#Exemplo:

opcao = -1
while opcao != 0: #Enquanto opcao for diferente de 0
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n:"))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Seu extrato é ...")
    else: None

#Ele vai repetir esse bloco até opcao for = a 0.

#Laço de repetição infinita:

contador_de_macacos = 0
while True:
    print("Contagem:", contador_de_macacos)
    contador_de_macacos += 1  # Incrementa o contador
    
    if contador_de_macacos >= 10:
        break

    
