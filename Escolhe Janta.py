import random
import Path

def addArquivo(lista)
    with open ('banco de lista.txt','w') as file:

        for v in lista:
                file.write (v)
                file.write ("\n")

def firstTime(inicio):
    
    lista = []
    x = 0
    y = 0

    while x == 0:
        inicio = str.lower(inicio)

        if inicio == "sim" or inicio == "vamos" or inicio == "bora":

            while y == 0:

                inicio = input ("Quais opções temos? ")

                if inicio == "":
                    y = 1
                    x = 1
                    print("Suas opções são:")
                    print (lista)

                else:
                    lista.append(inicio)

            z = (len(lista)) - 1

            decisão = random.randint(0, z)

            print (lista[decisão])

    addArquivo(lista)

    
def anterior():

    from pathlib

    if Path('banco de lista.txt').is_file():
        return True
    else:
        return False

def notFirst(inicio)
    antiga = input("Deseja utilizar a última lista? ")
    antiga = str.lower(antiga)

    if antiga == "sim":
        

def caminho():
    inicio = input ("Vamos descobrir o que jantar hoje? ")
    verificador = anterior()

    if verificador:
        notFirst()

    else:
        escolheJanta(inicio)


caminho()
