"""
while True:
    n_pessoas, n_datas = input("Digite primeiro o número de pessoas e, o número de datas: ").split("/")
    
    try:
    
        n_pessoas_int = int(n_pessoas)
        n_datas_int = int(n_datas)
    
    except:
        continue

    lista_datas = []
    
    
    
    for i in range (n_datas_int):
        dia,mes,ano = input(f"Digite o dia, o mês e o ano da data {i + 1}:") \
        .split("/")

        try:
            dia_int = int(dia)
            mes_int = int(mes)
            ano_int = int(ano)
        
        except:
             continue
        
        tupla_data = dia,mes,ano
        lista_datas.append(tupla_data)
        
       
        for data in lista_datas:
            dia,mes,ano = data

            soma_0 = 0
            soma_1 = 0
            lista_sim_nao_total = []

            for escolha_pessoa in range (n_pessoas_int):
                escolha_pessoa = int(input(f"Digite 1 para confimar presença na data {dia}/{mes}/{ano} ou 0 para o contrário:"))

                if escolha_pessoa == 1:
                    soma_1 += 1
                    soma_0 += 0
                
                else:
                    soma_0 += 1
                    soma_1 += 0

            tupla_sim_nao_data = soma_1,soma_0
            lista_sim_nao_total.append(tupla_sim_nao_data)

        
        for tupla in lista_sim_nao_total:            
            n_1 = tupla[0]
            n_1_max = 0

            if n_1 > n_1_max:
                n_1_max = n_1

"""

#01 - Entrada da quantidade de datas e pessoas votantes

from datetime import datetime

while True:
    n_pessoas, n_datas = int(input(f'Digite o número de pessoas e de datas:')).split(' ')
    #02 - Validação das variavéis de entrada 
    
    intervalo_n_pessoas = n_pessoas >= 1 and n_pessoas <= 50
    intervalo_n_datas = n_datas >= 1 and n_datas <= 50 
    
    if intervalo_n_pessoas and intervalo_n_datas:
        #03 - Input de datas 
        datas = {}
        
        for i in range (1,n_datas+1):
            
            data = input(f'Digite a data{i}:')
            
            #3.1 - Verficação da digitação de uma data no formato correto
            
            format_data = "%d/%m/%Y"
            res = bool(datetime.strptime(data,format_data))
            
            if res == False:
            
                continue
            else:
            
                datas.setdefault(f'data{i}', data)
    else:
    
        continue #Volta tudo de novo 
    #04 - Sistema de votação para cada data digitada 
    votos_dias = {} #04.1 - Formação de dicionário de votos com datas respectivas
    lista_votos_dia = []
    
    for chave_data in datas.values():
        print (f'{chave_data}')
        
        for i in range(n_pessoas):
            voto = int(input(f'Digite o voto da pessoa{i+1}:'))
            
            if voto != 0 or voto != 1:
                continue
            
            else:
                lista_votos_dia.append(voto)
        votos_dias.setdefault(f'Dia {chave_data} - {lista_votos_dia}')

#05 - Contagem de 0 e 1 de cada dia 
    n_aprovacoes_dia = 0
    lista_aprovacoes_por_dia = []    
    
    for x in votos_dias.values():
        
        for nums in x:
            
            if nums == 1:
                n_aprovacoes_dia  += 1
        lista_aprovacoes_por_dia.append(n_aprovacoes_dia)
#06 - Verficação de dia com mais votos 
    contador = 0
    dia = 0
    dia_com_maior_votacao = max(lista_aprovacoes_por_dia)
    
    for indice in range(len(lista_aprovacoes_por_dia)):
       
        if dia[indice] == dia_com_maior_votacao:
            indice_dia_escolhido = indice

#07 Associar o índice a chave do dicionário 
    for chave_data in votos_dias.keys():
        if contador == indice_dia_escolhido:
            print (f'{chave_data}')
        contador += 1    




                                                   


        





            









            





                
            
           





                    



            




       




