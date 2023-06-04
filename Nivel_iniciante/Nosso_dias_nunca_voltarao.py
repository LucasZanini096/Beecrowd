str = "LIFE IS NOT A PROBLEM TO BE SOLVED"

while True:
    num = int(input("Digite um número:"))

    if num >= 1 and num <= 34:
        print(str[0:num])
    else:
        print("Digite um número entre 1 e 34")
        continue
