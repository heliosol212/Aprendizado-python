print("<--Algoritmo Elemento Procurado-->")
lista_com = [1, 2, 3, 4, 5]

elemento_procurado = 4

encontrado = False

for elemento in lista_com:
    elemento = int(input("digite o valor do elemento: "))
    if elemento == elemento_procurado:
        encontrado = True
    break

if encontrado: 
    print(f"o elemento procurado foi encontrado, seu valor é : {elemento_procurado}")
else:
    print(f"o elemento procurado não foi encontrado, seu valor é : {elemento_procurado}")
    