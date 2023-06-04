"""
def main():
    a = [0,1,2,3,4,5,6]
    b = a.copy()
    b[1] = 5
    print (a)
    print (b)
    print (a.extend(b))

main()
""
def teste():
    linha = []
    for i in range (6):
        cinco_zeros = 0 * i
        linha.append(cinco_zeros)
        print(linha)


teste()
"""
def matriz_1():
    matriz = [[0,0],[0,0]]
    #linhas
    for i in range (0,2):
        #colunas
        for j in range (0,2): #Os dois primeiros for's são de estrutura das matrizes 
            matriz[i][j] = int(input(f'Digite um número na posição [{i},{j}]:'))
    #print ('-=' * 30 ) #linha de resultado 
    for i in range (0,2):
        for j in range (0,2):
            print (f'[{matriz[i][j]:^5}]', end ='') #O comando end serve para adicionar adicionar mais elementos a uma determinada string 
        print () #Serve para quebrar automaticamente uma linha 

matriz_1()



    


        

    

