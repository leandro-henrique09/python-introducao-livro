# Página 94

# Operadores relacionais

# Para realizarmos comparações lógicas, utilizaremos operadores relacionais;
# A lista de operadores relacionais suportados em Python é apresentada na Tabela 3.2

# Tabela 3.2: Operadores relacionais
# Operador       Operação      Símbolo matemático
#    ==          igualdade             =
#    >           maior que             >
#    <           menor que             <
#    !=          diferente             ≠
#    >=          maior ou igual        ≥
#    <=          menor ou igual        ≤

# O resultado de uma comparção com esses opretadores é um valor d tipo lógico,
# ou seja, True(verdadeiro) ou False(falso). Utilizaremos o verbo "avaliar" para indicar a resolução de uma expressão.
# Por exemplo:

a = 1 # a recebe 1 
b = 5 # b recebe 5 
c = 2 # c recebe 2
d = 1 # d recebe 1 
# 

# a == b
#  False

# a < b 
#  True

# a == d # a é igual a d?
#  True

# b >= a # b é maior ou igual a a?
#  True

# c <= b # c é menor ou igual a b?
#  True

# d != a # d é diferente de a/
#  False

# d != b # d é diferente de b?
#  True

# ==============================================================

# Página 95

# Variáveis de tipo lógica também podem ser utilizadas para armazenar o resultado de expressões e comparações:
nota = 8
media = 7
aprovado = nota >= media
print(aprovado)