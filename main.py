from problemas import *
tipoProblema = 0

while tipoProblema != 1 and tipoProblema != 2:
    tipoProblema = int(input("Digite:\n1- Para Problemas Elétricos \n2- Para Problemas Mecânicos\n"))

if tipoProblema == 1:
    print(problemaEletrico['Bateria'])

else:
    print(problemaMecanico['Motor'])