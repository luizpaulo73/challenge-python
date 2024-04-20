from problemas import *
from perguntas import *

tipoProblema = 0
verificador = range(1, 5)

carroMarca = input('Digite a marca do seu carro: ')
carroModelo = input('Digite o modelo do seu carro: ')

while tipoProblema != 1 and tipoProblema != 2:
    tipoProblema = int(
        input('Digite:\n1- Para Problemas Elétricos \n2- Para Problemas Mecânicos\n'))

if tipoProblema == 1:
    problema = int(input('Digite o número correspondente ao problema do carro:'
                         '\n1- Alternador'
                         '\n2- Motor de Arranque'
                         '\n3- Sistema de Iluminação'
                         '\n4- Sistema de Ignição\n'))

else:
    while True:
        problema = int(input('Digite o número correspondente ao problema do carro:'
                             '\n1- Motor'
                             '\n2- Transmissão'
                             '\n3- Suspensão e Direção'
                             '\n4- Freios'))
        if problema in verificador:
            break
        else:
            print('Digite um valor válido!')

    match problema:
        case 1:
            motor()
        case 2:
            transmissao()
