# O poder da composição realmente aparece quando precisamos combinar vários valores em uma nova string.
# Imagine que João tem 22 anos e apenas R$51,34 no bolso. Para exibir essa mensagem, podemos utilizar:

print("%s tem %d anos e apenas R$%5.2f no bolso" % ("João", 22, 51.34))

# Essa forma de composição foi substituída nas versões mais modernas do interpretador, e, embora
# continue a ser válida, tem caído em desuso.

# Uma forma mais moderna de compor strings é utilizando o método format.
# Vejamos o programa anterior, mas reescrito usando format em vez de %.

nome = "João"
idade = 22
grana = 51.34

print("{} tem {} anos e R${} no bolso.".format(nome,idade,grana))