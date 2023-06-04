#Linha da Matriz
def matriz_1():
    l = int(input("Digite a quantidade de linhas de uma matriz:"))
    c = int(input("Digite a quantidade de colunas de uma matriz:"))

    matriz = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
    #linhas
    for i in range (0,l):
        #colunas
        for j in range (0,c): #Os dois primeiros for's são de estrutura das matrizes 
            matriz[i][j] = int(input(f'Digite um número na posição [{i},{j}]:'))
    #print ('-=' * 30 ) #linha de resultado 
    for i in range (0,l):
        for j in range (0,c):
            print (f'[{matriz[i][j]:^5}]', end ='') #O comando end serve para adicionar adicionar mais elementos a uma determinada string
        print () #Serve para quebrar automaticamente uma linha 

matriz_1()
