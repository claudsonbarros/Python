"""
Crie um algoritmo que solicite 3 valores que representarão os lados de um triângulo.
Considere que não importa a ordem que serão fornecidos os valores,
podendo ser fornecido primeiro a hipotenusa e depois os catetos, ou primeiro os catetos e depois a hipotenusa, etc.
Crie também uma função que recebe o vetor e retorna se os lados informados formam um triângulo retângulo.
Você pode utilizar o teorema de Pitágoras para auxiliar na resolução: hiponusa2 = cateto12 + cateto22.
"""

def hipt(vetor,t):
    if vetor[0] > vetor[1] and vetor[0] > vetor[2]:
        hipo =vetor[0]
        vet1 = vetor[1]
        vet2 = vetor[2]
    elif vetor[1] > vetor[0] and vetor[1] > vetor[2]:
        hipo = vetor[1]
        vet1 = vetor[0]
        vet2 = vetor[2]
    else:
        hipo = vetor[2]
        vet1 = vetor[0]
        vet2 = vetor[1]

    if (vet1**2) + (vet2**2) == (hipo**2):
        print('É um triângulo retângulo')
    else:
        print('Não é um triângulo retângulo')






tam = 3
v = [0]*tam
for i in range(tam):
    v[i] = int(input('Informe o valor dos lados de um triangulo: '))


hipt(v, tam)
