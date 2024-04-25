from perguntas import *

tipoProblema = 0
verificador = range(1, 5)  # Verificador para garantir entrada válida

# Solicitando informações do carro ao usuário
carroMarca = input('Digite a marca do seu carro: ')
carroModelo = input('Digite o modelo do seu carro: ')

# Loop para garantir que o usuário digite uma localização válida
while True:
    localizacao = int(input('Digite o número correspondente a sua região:'
                            '\n1- Zona Norte'
                            '\n2- Zona Oeste'
                            '\n3- Zona Leste'
                            '\n4- Zona Sul\n'))
    if localizacao in verificador:  # Verificando se a entrada está dentro do intervalo permitido
        break
    else:
        print('Digite um valor válido!')

    # Convertendo o número da região para o nome correspondente
match localizacao:
    case 1:
        localizacao = 'Zona Norte'
    case 2:
        localizacao = 'Zona Oeste'
    case 3:
        localizacao = 'Zona Leste'
    case 4:
        localizacao = 'Zona Sul'

# Loop para garantir que o usuário escolha um tipo de problema válido
while tipoProblema != 1 and tipoProblema != 2:
    tipoProblema = int(input('Digite:\n1- Para Problemas Elétricos \n2- Para Problemas Mecânicos\n'))

# Verificando o tipo de problema e solicitando mais informações específicas
if tipoProblema == 1:
    while True:
        problema = int(input('Digite o número correspondente ao problema do carro:'
                            '\n1- Alternador'
                            '\n2- Motor de Arranque'
                            '\n3- Sistema de Iluminação'
                            '\n4- Sistema de Ignição\n'))
        if problema in verificador:
            break
        else:
            print('Digite um valor válido!')

    # Chamando a função correspondente ao problema elétrico selecionado
    match problema:
        case 1:
            alternador()
        case 2:
            motorArranque()
        case 3:
            sistemaIluminacao()
        case 4:
            sistemaIgnicao()

else:
    while True:
        problema = int(input('Digite o número correspondente ao problema do carro:'
                             '\n1- Motor'
                             '\n2- Transmissão'
                             '\n3- Suspensão e Direção'
                             '\n4- Freios\n'))
        if problema in verificador:
            break
        else:
            print('Digite um valor válido!')

    # Chamando a função correspondente ao problema mecânico selecionado
    match problema:
        case 1:
            motor()
        case 2:
            transmissao()
        case 3:
            suspencao_e_direcao()
        case 4:
            freios()

# Exibindo mensagem final com informações do problema e localização
print(f'Problema detectado! \nTraga seu {carroMarca} {carroModelo} para alguma oficina credenciada da Porto Seguro na {localizacao}')
