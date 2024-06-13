# A tag "is" tem a função de verificar se uma variável tem mesmo o mesmo valor de outra coisa. Exemplo:
curso = "curso python"
nome_curso = curso

print(curso is nome_curso)
#true

# também é possível utilizar outros operadores junto com o de identidade. Como o de negação:
psi = "maria"
psni = "nicolas"
print(psi is not psni)
#true


print(str is "")


a = 10
c = 10

print (c == a)
print (c is a)

#Nota: '==' Compara valores
#Nota: 'is' Verifica a identidade de objetos