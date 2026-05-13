# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

# Resposta:
salario = float(input("Digite o salário atual:"))
aumento = float(input("Digite a porcentagem de aumento:"))
novo_salario = salario + (salario * aumento / 100)

print(f"O novo salário vai ser no valor de R${novo_salario}")

# 


# Gabarito: 
salário = float(input("Digite o salário atual:"))
p_aumento = float(input("Digite a porcentagem de aumento:"))
aumento = salário * p_aumento / 100
novo_salário = salário + aumento
print("Um aumento de %5.2f %% em um salário de R$ %7.2f" % (p_aumento, salário))
print("é igual a um aumento de R$ %7.2f" % aumento)
print("Resultando em um novo salário de R$ %7.2f" % novo_salário)