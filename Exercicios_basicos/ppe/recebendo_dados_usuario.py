# Recebendo dados de usuário
print('Qual o seu nome ')
nome = input()

# Saida
print('Seja bem-vindo(a) %s' %nome)

print('Qual a sua idade?')
idade = input()

#print velho
#print('A %s tem %s anos'%(nome,idade))

#print normal
#print('A {0} tem {1} anos'.format(nome,idade))

#print mais recente diponivel a a partir do 3.x
print(f'A {nome} tem {idade} anos ')
print(f'A {nome} nasceu em  {2019 - int(idade)}')