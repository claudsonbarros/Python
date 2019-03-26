# Calculadora
# Variaveis
contador = 0
resultado = 0


def calcula(op, valor1, valor2):
    global contador
    global resultado
    contador = 1
    while op != '0':
        if op == '+':
            resultado = valor1 + valor2
            print(f'O resultado é: {resultado}')
        elif op == '-':
            resultado = valor1 - valor2
            print(f'O resultado é: {resultado}')
        elif op == '*':
            resultado = valor1 * valor2
            print(f'O resultado é: {resultado}')
        elif op == '/':
            resultado = valor1 / valor2
            print(f'O resultado é: {resultado}')
        print('\n')
        entrada()
        op = '0'


def entrada():
    global contador
    operacao = input('Informe a operação desejada:')

    if (contador != 1) or (contador == 1 and operacao.upper() == 'C'):
        if (operacao == '-' or operacao == '/' or operacao == '+' or operacao == '*' or operacao.upper() == 'C'):
            if operacao.upper() == 'C':
                operacao = input('Informe a nova operação desejada:')
                if (operacao != '-' and operacao != '/' and operacao != '+' and operacao != '*' and operacao.upper() != 'C'):
                    print('Operação Inválida\n')
                    contador = 0
                    entrada()
            primeiro = float(input('Informe o primeiro valor:'))
            segundo = float(input('Informe o segundo valor:'))
            calcula(operacao, primeiro, segundo)
        elif operacao == '0':
            print('Calculadora Encerrada')
        else:
            print('Operação Inválida\n')
            entrada()

    elif contador == 1 and operacao.upper() != 'C':
        if (operacao == '-' or operacao == '/' or operacao == '+' or operacao == '*'):
            segundo = float(input('Informe o valor:'))
            calcula(operacao, resultado, segundo)
        elif operacao == '0':
            print('Calculadora Encerrada')
        else:
            print('Operação Inválida\n')
            entrada()


def inicio():
    print('Bem-Vindo(a) a Calculadora\n'
          '_______________________\n',
          'Operações aceitas: \n',
          'Soma: + \n',
          'Subtração: - \n',
          'Multiplicação: * \n',
          'Divisão: / \n',
          'Encerrar: 0 \n',
          'Limpar Memoria: C\n'
          '_______________________\n')
    entrada()


inicio()
