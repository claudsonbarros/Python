"""
crie um algoritmo que leia um valor e a partir disso faça:
(1) se for um valor negativo, mostre o módulo (valor sem sinal) do valor;
(2) se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;
(3) Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5.
"""

def calcula(valor):
    if valor >= 0 and valor <=10:
        print(valor/5)
    elif valor < 0:
        print(valor * -1)
    elif valor > 10:
        valor2 = int(input('Informe outro numero: '))
        print(f'A diferença entre {valor} e {valor2} é {valor - valor2}')

calcula(int(input('Informe um valor inteiro: ')))

