import math
"""
crie um algoritmo que leia um valor e a partir disso faça: (1) se o valor for 1, 2 ou 3, 
mostre o valor elevado ao quadrado; (2) se o valor for o número 4 ou 9, 
mostre a raiz quadrada do número; (3) se for os valores 6, 7 e 8, mostre o valor dividido 9.
"""

def valida(valor):

    if valor == 1 or valor == 2 or valor == 3:
        print(f'O resultado de {valor} ao quadrado é {valor**2}')
    elif valor == 4 or valor == 9:
        print(f'a raiz quadrada de {valor} é {math.sqrt(valor)}')
    elif valor == 6 or valor == 7 or valor == 8:
        print(f'O valor de {valor}/9 é {valor/9}')

valida(int(input('Informe um valor numerico: ')))








