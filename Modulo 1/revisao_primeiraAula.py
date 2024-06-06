#revisao

int() #número inteiro, ex:

a = int("1")
print(a) #a = "1", um numero inteiro

float() #número real que pode representar numeros decimais, ex:

b = float("2.5")
print(b) #b = "2.5", um numero real(decimal).

bool() #True ou False, exemplo

print(bool(0)) #falso
print(bool(1)) #verdadeiro

#outro modo:

#esta_sol = True #verdadeiro
#ou
esta_sol = bool(1)

if esta_sol: #se esta sol entao
    print("Está sol")
else: #senao
    print("Não está sol")

#Strings, texto

c = str("Olá Mundo!")
print(c)

#se você tentar somar strings, ele irá concatenar o texto

d = str=("Hello World!")
print(c+d)

#listas com ints e floats

#lista_int = [1, 3 , 2] // inteiro
#print(lista_int)

#lista_float = [1.3, 3.2, 2.4] // float ou real(decimal)
#print(lista_float)

#está fora de ordem, então se quiser ordenar faça:

lista_int = [1, 3, 2]
lista_int_ordenada = sorted(lista_int)
print(lista_int_ordenada)

#agora float

lista_float = [1.3, 3.2, 2.4]
lista_float_ordenada = sorted(lista_float)
print(lista_float_ordenada)

# se quiser de forma decrescente faça

lista_float_decrescente = sorted(lista_float, reverse= True)
print(lista_float_decrescente)

lista_int_decrescente = sorted(lista_int_ordenada, reverse= True)
print(lista_int_decrescente)


