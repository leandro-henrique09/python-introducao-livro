# Entrada de dados.

# A função input é utilizada para solicitar dados do usuário. Ela recebe um parâmetro,
# que é a mensagem a ser exibida, e retorna o valor digitado pelo usuário.
# Vejamos um exemplo:

x = input('Digite um número: ')
print(x)

# 

# Vejamos outro exemplo:
nome = input('Digite seu nome: ') # aqui solicitamos a entrada de dados, no caso, o nome do usúario.
print(f'Você digitou {nome}')
print(f'Olá {nome}')

# 

# Conversão da entrada de dados.
# A função input retorna valores do tipo string, ou seja, não importa se digitamos apenas números, o resultado sempre é do tipo string.
# Para resolver esse pequeno problema, vamos utilizar a função int para converter o valor retornado em um número inteiro, e a função
# float para convertê-lo em número decimal ou de ponto flutuante.

# Vejamos outro exemplo:
anos = int(input('Anos de serviço: '))
valor_por_ano = float(input('Valor por ano: '))
bonus = anos * valor_por_ano
print(f"Bônus de R${bonus:5.2f}")