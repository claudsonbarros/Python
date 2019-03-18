"""crie uma função que retorne o valor da expressão: 2/3 + 3/5 + 4/7 + 5/9 + … + n/m,
 para um valor de n definido pelo usuário. Verifique se o valor de n definido pelo usuário é positivo e,
 aso não seja, solicite outro valor até ser fornecido um valor positivo."""

def calcula(val):
    vAux1=2
    vAux2=3
    calculo = 0
    var = ''
    sinal=''

    while vAux1 <= val:
        var = var + str(sinal) + str(vAux1) + '/' + str(vAux2)

        calculo = calculo + (vAux1/vAux2)
        vAux1 += 1
        vAux2 += 2
        sinal = ' + '

    print(f'A formula utilizada foi: {var}')
    print(calculo)


def validaInput():
    valor = int(input('Informe um valor positivo: '))
    while valor <= 0:
        print(f'O valor {valor} é inválido.\n')
        valor = int(input('Informe um valor positivo: '))
    calcula(valor)


validaInput()
