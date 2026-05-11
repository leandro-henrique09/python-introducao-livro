# Página 102

# Para acessar os caracteres de uma string, devemos informar o índice ou posição
# do caractere entre colchetes ([]). 

# Exemplo:
a = "ABCDEF"
# 

a[0]
# saida: 'A'

# 
a[1]
# saida: 'B'

# 
a[5]
# saida: 'F'

# 
len(a)
# saida: '6'

# 
# Como a variavel 'a' tem 6 caracteres, devemos acessar pelo caracter na posição de 0 a 5, contando que o indice começa em 0.

# 

# Concatenação
# Os conteúdos de variáveis string podem ser somados, ou melhor, concatenados. 
# Para concatenar duas strings, utilizamos o operador de adição(+).
# Assim "AC" + "C" é igual a "ABC". Um caso especial de concatenação é a repetição de uma string várias vezes.
# Para isso, utilizamos o operador de mutiplicação(*): "A" * 3 é igual a "AAA".

# Exemplos:
s = "ABC"

# 

s + "C"
# saida: "ABCC" - foi concatenado o C junto a varíavel 's'.

# 

s + "D" * 4
# saida: 'ABCDDDD' - foi adicionado 4 "D" na variavel "s".

# 

# Esta forma de concatenação só pode ser usada com strings.

