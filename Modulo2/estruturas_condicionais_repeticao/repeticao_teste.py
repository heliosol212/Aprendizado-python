#Definir o numero de inputs (entradas):
def capturar_valores():
    nde = input("Quantas entradas você quer?")
    entradas = []

    for i in range(nde):
        entrada = input(f"Digite o valor {i+1}: ")
        entradas.append(valor)
    return entradas

lista_valores = capturar_valores()

print("Valores inseridos:", lista_valores)

