# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do
# desconto e o preço a pagar.

# Resposta:
preco = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_final = preco - (preco * desconto / 100)
print(f"O valor da mercadoria era de R${preco}, mas com o desconto ficou R${valor_final}")

# 

# Gabarito: 
preço = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))
valor_do_desconto = preço * desconto / 100
a_pagar = preço - valor_do_desconto
print("Um desconto de %5.2f %% em uma mercadoria de R$ %7.2f" % (desconto, preço))
print("vale R$ %7.2f." % valor_do_desconto)
print("O valor a pagar é de R$ %7.2f" % a_pagar)