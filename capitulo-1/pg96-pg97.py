# Página 96

# Operadores lógicos

# Para agrupar operações com lógica booleana, utilizaremos operadores lógicos.
# Python suporta três operadores básicos: not(não), and(e), or(ou). Esses ope-
# radores podem ser traduzidos como não(negação), e(conjunção) e ou(disjunção).

# Tabela 3.3: Operadores Lógicos
        # Operador Python     Operação        
        #       not              não  
        #       and              e  
        #       or               ou 

# =====================================================================================

# Página 97

# Tabela 3.4: Tabela verdade do operador not(não)
        #       V                  not V        
        # True(verdadeiro)     False(falso)  
        # False(falso)         True(verdadeiro)

# Exemplo:
    # not True # se não for True é False
    #   False

    # not False # se não for False é True.
    #   True

# 

# Tabela 3.5: Tabela verdade do operador and(e)
                V                       V                       V and V 
        True(verdadeiro)        True(verdadeiro)           True(verdadeiro)
        True(verdadeiro)          False(falso)               False(falso)
          False(falso)          True(verdadeiro)             False(falso)
          False(falso)            False(falso)               False(falso)

# Exemplo:

# True and True
#       True

# True and False
#       False

# False and True
#       False

# False and False
#       False