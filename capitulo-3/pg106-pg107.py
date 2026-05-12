# Como python é uma linguagem que não para de evoluir, uma terceira forma de compor strings foi adicionada na versão 3.6
# Ela se chama f-string, pois escrevemos a letra f antes de abrirmos as aspas.
# Vejamos o programa anterior, mas dessa vez usando f-strings.

# Programa anterior: 
    # nome = "João"
    # idade = 22
    # grana = 51.34

    # print("{} tem {} anos e R${} no bolso.".format(nome,idade,grana))

nome = "João"
idade = 22
grana = 51.34

print(f"{nome} tem {idade} anos e R${grana} no bolso.")

# =================================================================== 

# Página 107

# Fatiamento de strings.

# O fatiamento em Python é muito poderoso e permite dividirmos uma string
# em pedaços menores. Imagine nossa string de exemplo da Figura 3.2.
# Podemos fatiá-la de forma a escrever apenas seus dois primeiros caracteres AB utilizando como índice [0:2].

# Figura 3.2
s = "ABCDEFGHI"

print(s[0:2]) # aqui estamos fatiando a string partindo do indice 0 e indo até o indice 1, lembrando que o ultimo número é sempre um indice anterios
# saida: "AB"
# 

print(s[1:2]) # aqui estamos fatiando do índice 1 até ele mesmo, contando que o número da direita é sempre um a menos, resultando em 1.
# saida: "B"
# 

print(s[2:4]) # aqui estamos fatiando do índice 2 até o índice 3.
# saida: "CD"
# 

print(s[0:5]) # aqui estamos fatiando do índice 0 até o índice 4
# saida: "ABCDE"
# 

print(s[1:8]) # aqui estamos fatiando do índice 1 até o índice 7.
# saida: "BCDEFGH"

# ================================================================