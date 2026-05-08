# Página 98

# A tabela verdade do operador or(ou em português) é apresentada na Tablea 3.6.
# A regra fundamental do operador or (ou) é que ele se resulta em falso apenas se 
# seus dois operando também forem falsos. Se apenas um de seus operandos for
# verdadeiro, ou se os dois forem, o resultado da operação será verdadeiro.

# Tabela 3.6: Tabela verdade do operador or(ou)
                V                       V                       V or V 
        True(verdadeiro)        True(verdadeiro)           True(verdadeiro)
        True(verdadeiro)          False(falso)             True(verdadeiro)
          False(falso)          True(verdadeiro)           True(verdadeiro)
          False(falso)            False(falso)               False(falso)

# Exemplo:
# True or True
#   True

# True or False
#   True

# False or True
#   True

# False or False
#   False

# 

# =================================================================================
# Página 99

# Os operadores lógicos podem ser combinados em expressões lógicas mais complexas.
# Quando uma expressão tiver mais de um operador lógico, avalia-se o operador not(não) primeiro,
# seguido do operador and(e) e, finalmente, or(ou).
# Vejamos a seguir a ordem de avaliação da expresão, em que a operação sendo avaliada é sublinhada;
# e o resultado, mostrado na linha seguinte

True or False and not True 
  True or False and False 
      True or False
          True

# Os operadores relacionais também podem ser utilizados em expressôes com operadores lógicos.
# -- salario > 1000 and idade > 18

# Nesses casos, os operadores relacionais devem ser avaliados primeiro.
# Façamos salario = 100 e idade = 20. Teremos:
salario > 1000 and idade > 18
    100 > 1000 and 20 > 18
        False and True
             True

