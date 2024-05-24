from perguntas import *
tipoProblema = 0
verificador = range(1, 5)  # Verificador para garantir entrada válida

# Solicitando informações do carro ao usuário
def inputs():
    carroMarca = input('Digite a marca do seu carro: ')
    carroModelo = input('Digite o modelo do seu carro: ')
    return carroMarca , carroModelo


# Loop para garantir que o usuário digite uma localização válida
def localizacao():
    regioes = ['Zona Norte' , 'Zona Oeste' , 'Zona Leste' , 'Zona Sul']
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
    if localizacao == 1:
        return regioes[0]
    elif localizacao == 2:
        return regioes[1]
    elif localizacao == 3:
        return regioes[2]
    elif localizacao == 4:
        return regioes[3]

# Loop para garantir que o usuário escolha um tipo de problema válido
def eletrico_mecanico(tipoProblema):
    while tipoProblema != 1 and tipoProblema != 2:
        tipoProblema = int(input('Digite:'
                                '\n1- Para Problemas Elétricos' 
                                '\n2- Para Problemas Mecânicos\n'))
    return tipoProblema

def eletrico():
    # Verificando o tipo de problema e solicitando mais informações específicas
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

def mecanico():
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


# ==================== #
#       PRINCIPAL      #
# ==================== #
carroMarca, carroModelo = inputs()  # Obtendo informações do usuário
regiao = localizacao()
tipoProblema = eletrico_mecanico(tipoProblema)
if tipoProblema == 1:
    eletrico()
elif tipoProblema == 2:
    mecanico()

print(f'Problema detectado! \nTraga seu {carroMarca} {carroModelo} para alguma oficina credenciada da Porto Seguro na {regiao}')