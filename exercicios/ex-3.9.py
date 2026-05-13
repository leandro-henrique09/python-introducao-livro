# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total
# em segundos.

# Resposta:
qtd_dias = int(input("Digite a quantidade de dias:"))
qtd_horas = int(input("Digite a quantidade de horas:"))
qtd_minutos = int(input("Digite a quantidade de minutos:"))
qtd_segundos = int(input("Digite a quantidade de segundos:"))
total_segundos = qtd_dias * 24 * 3600 + qtd_horas * 3600 + qtd_minutos * 60 + qtd_segundos
print(f"Convertido em segundos é igual a {total_segundos} segundos.")

# Gabarito: 
dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))
# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Convertido em segundos é igual a %10d segundos." % total_em_segundos)