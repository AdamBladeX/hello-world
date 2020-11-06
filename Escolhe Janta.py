import random
from pathlib import Path

def addArquivo(lista):
    
    with open ('banco de lista.txt','w') as file:

        for v in lista:
            file.write (v)
            file.write (";")
                
def firstTime():

    inicio = input ("Vamos descobrir o que jantar hoje? ")
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

        else:
            stop()
    
def anterior():

    if Path('banco de lista.txt').is_file():
        return True
    else:
        return False

def notFirst():

    with open('banco de lista.txt',"r") as file:
        content = file.read()
        contentList = content.split(";")

    del contentList[-1]
    print("Suas opções foram: ",contentList)
    antiga = input("Deseja utilizar a última lista? ")
    antiga = str.lower(antiga)

    if antiga == "sim":
        
        z = (len(contentList)) - 1
        decisão = random.randint(0, z)
        print (contentList[decisão])

    else:
        firstTime()

def caminho():
    
    verificador = anterior()

    if verificador:
        notFirst()

    else:
        firstTime()


caminho()
