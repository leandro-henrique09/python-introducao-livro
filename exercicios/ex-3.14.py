# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$ 60 por dia e R$ 0,15 por km rodado.

# Resposta:
km_percorrido = float(input("Quantos kms foi percorrido? "))
qtd_dias = int(input("Quantos dias andou? "))
preco_final = 60 * qtd_dias + 0.15 * km_percorrido
print(f"O total do aluguel foi de R${preco_final}.")

# 

# Gabarito:
km = int(input("Digite a quantidade de quilometros percorridos:"))
dias = int(input("Digite quantos dias você ficou com o carro:"))
preço_por_dia = 60
preço_por_km = 0.15
preço_a_pagar = km * preço_por_km + dias * preço_por_dia
print("Total a pagar: R$ %7.2f" % preço_a_pagar)