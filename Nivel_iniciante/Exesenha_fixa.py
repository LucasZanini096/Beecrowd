#Senha Fixa 
senha_digitada = int(input("Digite uma senha de quatro dígitos:"))
senha_correta = 2002

while senha_digitada != 0:
    if senha_digitada == senha_correta:
        print ("Acesso permitido")
        break
    else: 
        print ("Senha Inválida")
        senha_digitada = int(input("Digite novamente uma senha:"))
        continue 
