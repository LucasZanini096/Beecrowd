lista_competidores = []
num_competidores = int(input("Digite o número de competidores:"))
num_competidores = num_competidores if num_competidores >= 1 and num_competidores <= 500 \
    else print("Fim do programa")

for indice in range (num_competidores):
    competidor = int(input(f'Digite a velocidade do competidor[{indice}] em cm/h:'))
    competidor = competidor if competidor >= 1 and competidor <= 50 else print("Fim do programa")

    lista_competidores.append(competidor) 

print(lista_competidores)
maior_velocidade = max(lista_competidores)

if maior_velocidade < 10:
    print("Sua velocidade é de nível 1")

elif maior_velocidade >= 10 and maior_velocidade < 20:
    print("Sua velocidade é de nível 2")

else:
    print("Sua velocidade é de nível 3")
