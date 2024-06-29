#Definir o numero de inputs (entradas):
def capturar_valores():
    nde = int(input("Quantas entradas você quer?"))
    entradas = []

    for i in range(nde):
        entrada = int(input(f"Digite o valor {i+1}: "))
        entradas.append(entrada)
    return entradas

lista_valores = capturar_valores()

print("Valores inseridos:", lista_valores)