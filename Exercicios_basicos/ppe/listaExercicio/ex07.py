file = open("C:/Users/claudson.barros/Documents/Estudo/ODI/Recebido/Lista.txt" , 'r')
texto = file.readlines()
i = 0
lista = list()


for linha in texto:
    lista.append(linha.rstrip("\n\r"))
file.close()


print(lista)


for l in lista:
    if lista.index(l) != 0:
        print(l)

