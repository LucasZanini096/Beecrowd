#Sequência lógica 
import math 
n = int(input("Digite uma número:"))
x = 0
if n == 1:
    print (1,1,1)
    print (1,2,2) 
else:
    for x in range (1, n + 1):
        for i in range(1,n + 1):
            print (math.pow(i,x), math.pow(i,x+1), math.pow(i,x+2))
            print (math.pow(i,x), math.pow(i,x+1) + 1, math.pow(i,x+2) + 1)
