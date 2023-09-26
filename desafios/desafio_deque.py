""" 
Resolva o clássico problema de palíndromos. Um número ou palavra é palíndromo quando apresenta
a mesma ordem lida da direita para a esquerda ou da esquerda para a direita.

No seu teste, você deverá escrever um programa em Python que receba como entrada um conjunto 
de caracteres, a ser digitado pelo usuário, e informe se o número é ou não é palíndromo, 
usando filas do tipo deque.

"""

from collections import deque

def verificar_palindromo(d):
    deque_1 = deque(d)
    deque_2 = deque(reversed(deque_1))
    if deque_1 == deque_2:
        return True
    return False


deque_f = input("Digite a sequência: ")

print(verificar_palindromo(deque_f))
