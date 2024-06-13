# geralmente usados com os opeeradores de comparação
# são adicionados assim:
# operador de comparacao + operador logico + operador comparacao ...
#exemplo:

saldo = 1000
saque = 200
limite = 100

#saldo >= saque and saque <= limite

#saldo é maior ou igual a saque? e saque e menor ou igual a limite?

#o operador "and" necessitada que ambas partes sejam verdadeiras. 
#então saldo tem que ser maior que saque e saque menor ou igual limite.
#caso contrário não vai funcionar.

#"Or"

expr = saldo >= saque or saque <= limite
print(expr)
#apenas uma das condições pode ser verdadeira, o resto pode ser falso.