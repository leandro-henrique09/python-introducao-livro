# Podemos também omitir o número da esquerda ou o da direita para representar do ínicio ou até o final.
# Assim,[:2] indica do ínicio até o segundo caractere (sem inclui-lo), e [1:] indica do caractere de posição 1 até o final da string.
# Observe que, nesse caso, nem precisamos saber quantos caracteres a string contém. Se omitirmos o início e o fim da fatia [:],
# estaremos fazendo apenas uma cópia de todos os carcteres da string para uma nova string.

s = "ABCDEFGHI"

print(s[:2]) # aqui estamos pegando do inicio e indo até o índice 1.
# saida: AB 

#  

print(s[1:]) # aqui estamos indo do índice 1 até o final da string.
# saida: BCDEFGHI

# 

print(s[:]) # aqui estamos pegando do começo ao fim da string.
# saida: ABCDEFGHI

# Podemos também utilizar valores negativos para indicar posições a partir da direita.
# Assim, -1 é o ultimo caractere;-2, o penúltimo; e assim por diante. Veja o resultado de testes com 
# índices negativos:

print(s[0:-2]) # aqui estamos indo do primeiro índice até o pénúltimo.
# saida: ABCDEFG
# 

print(s[-1:]) # aqui estamos acessando somente o ultimo índice.
# saida: I 
# 

print(s[-5:7]) # aqui estamos indo do índice -5 até o 6, contando o -5 do final.
# saida: EFG
# 

# Podemos inverter uma string usando um recurso simples de fatias, no caso, um terceiro parametro. Usando -1, envertemos a string.

print(s[::-1])
# saida: IHGFEDCBA

# Esse terceiro parâmetro pode ser um número positivo, pois define o incremento de um elemento para outro.
# no caso de 2, ele pega um a cada 2 elementos.
print(s[::2])
# saida: ACEGI