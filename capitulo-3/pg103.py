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

# Juntar várias strings para construir uma mensagem nem sempre é pratico. Por exemplo, exibir que "João tem X anos",
# em que X é uma variável numérica.

# Marcadores

# Tabela 3.7: Marcadores
        # Marcador |        Tipo
        #     %d   |   Números inteiros
        #     %s   |        Strings
        #     %f   |   Números decimais

# Exemplos: 

x = 10
print("%d é a idade de joão" % x) # aqui usei o marcador de números inteiros para mostrar a idade de joão.

print("%03d" % x) # aqui tornamos o "x" é 3 posições onde completa com 0 á esquerda.
# saida: 010

print("%3d" % x) # aqui também estamos determinando que "x" vai ter 3 posições, mas sem o 0 á esquerda;
# saida: 10.

print("%-3d" % x) # aqui estamos determinando que tera espaços em branco á direita do valor.
# saida:10 .


