# Exercício 3.5 - Página 100

# Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir.

# Resposta
A  |  B  |   C   |    D    |  Resultado
1  |  2  | True  |  False  |    True
10 |  3  | False |  False  |    True
5  |  1  | True  |   True  |    True

# Gabarito
# False
# False
# True

# Esse exercicio não compreendi muito bem, por isso não cheguei ao resultado esperado, mas ao ler sobre, entendi
# do por que ter errado, foi mais falta de interpretação do enunciado. 

# As etapas me confundiram um pouco, porém agora entendi o funcionamento da lógica.

# Lógica:
# A > B and C or D
    1 > 2   and   True     or False # fazendo de exemplo com a primeira linha
    False         True      ^    
            ^               # O operador or retorna True se pelo menos um lado for verdadeiro, 
            ^               # como os dois foram falsos o resultado retornado foi False.
            ^    
            ^
    # Voltando um pouco na tabela do and
    # fica claro que and precisa que os dois sejam verdadeiros.
    # Portanto o resultado será False.