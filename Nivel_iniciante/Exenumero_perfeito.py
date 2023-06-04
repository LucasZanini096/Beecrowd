#Número perfeito 
#01 - Colocar um número 
num = int(input("Digite um número:"))
#02 - Divisores de um número
lista = [i for i in range(1, num//2+1) if num%i==0]
"""
Os dois i's, pois o primeiro é referente ao 1, 
já o outro é referente a expressão num//2+1, ambos subordiandos a uma condição if
"""
#03 - Soma 
soma = sum(lista)
#04 - Condição para número perfeito 
if sum(lista) == num:
    print (f'{num} é um número perfeito.')
else:
    print(f'{num} não é um número perfeito.')