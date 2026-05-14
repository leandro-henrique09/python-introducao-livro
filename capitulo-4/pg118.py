# If

# As condições servem para selecionar quando uma parte do programa deve serve
# ativada e quando deve ser simplesmente ignorada. Em Python, a estrutura de
# decisão é o IF. Seu formato é apresentado a seguir:

    # if <condição>:
    #     bloco verdadeiro

# Vejamos um exemplo de programa que lê dois valores e imprime qual é o maior:

# Programa 4.1: Lê dois valores e imprime qual é o maior
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
    print("O primeiro valor é o maior!")
if b > a:
    print("O segundo valor é o maior!")