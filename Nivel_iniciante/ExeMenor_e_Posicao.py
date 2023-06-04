#01 - Entrada do número de elementos 
n_elementos = int(input("Digite o número de elementos:"))
#02 Repetição da entrada de elementos 
sequencia = '' #primeiro print
lista_sequencia_separada = [] #segundo e terceiro print
for i in range (n_elementos):
    num_objeto = int(input("Digite um número:"))
    sequencia += str(num_objeto) + ' '
    lista_sequencia_separada.append(num_objeto)

print(sequencia)
#03 Vizualizar o menor valor e sua posição respectiva 
menor_valor = min(lista_sequencia_separada) 
print(f'Menor valor: {menor_valor}')
#3.1 - Posição do menor valor 
for indice, posicao_menor in enumerate(lista_sequencia_separada):
    if posicao_menor == menor_valor:
        print (f'Posição: {indice}')




 
