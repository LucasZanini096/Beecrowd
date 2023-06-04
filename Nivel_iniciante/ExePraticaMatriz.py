"""
def gerar_matriz (n_linhas, n_colunas):
        ''' 
          (int,int) -> matrix
        '''

        matriz = []
        matriz.append(" ")
        matriz.append([" "]*num_linhas)

        i = 0
        while i < len(matriz):
            matriz[i].append(" ")
            i += 1


        return matriz
"""

def Matriz_quadrada():

    n_linhas_colunas = int(input("Digite o número de linhas e colunas:"))
    matriz = []
    n_zeros = [0]*n_linhas_colunas
    

    for i in range (n_linhas_colunas):
        matriz.append(n_zeros)
    
    print (matriz)
    
    for linha in range (n_linhas_colunas):
        for coluna in range (n_linhas_colunas):
            matriz[linha][coluna] = \
            int(input(f"Digite o valor da posição [{linha},{coluna}]:"))


    print ('-=' * 30 )
    for linha in range (n_linhas_colunas):
        for coluna in range (n_linhas_colunas):
            print (f'[{matriz[linha][coluna]:^5}]', end ='') 
        print()
    print ('-=' * 30 )


Matriz_quadrada()

