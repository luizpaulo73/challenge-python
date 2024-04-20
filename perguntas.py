def motor():
    verificador = range(1,6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                        '\n1- Se o motor está fazendo algum barulho incomum'
                        '\n2- Se alguma fumaça está saindo do motor'
                        '\n3- Se o veículo está tendo dificuldades para ligar'
                        '\n4- Se o motor está perdendo potência'
                        '\n5- Se há vazamentos visíveis de fluidos do motor\n'))
        if resposta in verificador:
            break
    
    match resposta:
        case 1:
            print('A correia dentada do seu veículo esta com perda de tensão')
        case 2:
            print('Seu veículo está queimando óleo devido a vazamentos ou desgaste de peças internas')
        case 3:
            print('As velas de Ignição do seu veículo estão gastas')
        case 4:
            print('O sistema de combustível esta com problemas')
        case 5:
            print('Seu veículo esta com vazamento de óleo do carter')

def transmissao():
    verificador = range(1,6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                        '\n1- Se o pedal da embreagem está ficando preso ou afundando facilmente'
                        '\n2- Se você percebe um cheiro de queimado ao dirigir'
                        '\n3- Se o veículo está tendo dificuldades para engatar as marchas'
                        '\n4- Se você nota trepidação ou vibração ao soltar a embreagem'
                        '\n5- Se o veículo está se movendo mesmo com o pedal da embreagem totalmente pressionado\n'))
        if resposta in verificador:
            break
    
    match resposta:
        case 1:
            print('Seu veículo esta com o cabo de embreagem desgastado ou danificado')
        case 2:
            print('Seu veículo esta com desgaste excessivo do disco da embreagem')
        case 3:
            print('Seu veículo esta com desgaste do disco ou platô da embreagem')
        case 4:
            print('Disco da embreagem empenado')
        case 5:
            print('Vazamento de fluido hidráulico da embreagem')

def suspencao_e_direcao():
    verificador = range(1,6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                        '\n1- Você sente vibrações excessivas no volante ao dirigir em alta velocidade'
                        '\n2- O veículo está inclinando ou puxando para um lado ao fazer curvas'
                        '\n3- Você ouve ruídos de batidas ou rangidos ao passar por solavancos ou irregularidades na estrada'
                        '\n4- O volante está difícil de girar ou há folga excessiva na direção'
                        '\n5- Você nota vazamentos de fluido sob o veículo próximo às rodas dianteiras\n'))
        if resposta in verificador:
            break
    
    match resposta:
        case 1:
            print('Seu veículo esta com desgaste ou desalinhamento dos pneus')
        case 2:
            print('Seu veículo esta com os amortecedores desgastados ou com vazamento')
        case 3:
            print('Seu veículo esta com as buchas da suspensão desgastadas')
        case 4:
            print('Seu veículo esta com baixo nível de fluido de direção hidráulica')
        case 5:
            print('Seu veículo esta com vazamento de fluido de direção hidráulica')

def freios():
    verificador = range(1,6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                        '\n1- Você nota que o pedal do freio está afundando até o fundo ou parece esponjoso'
                        '\n2- Você ouve um ruído agudo ou rangido ao frear'
                        '\n3- Você sente vibração no volante ou no pedal do freio ao frear em alta velocidade'
                        '\n4- O veículo está puxando para um lado ao frear'
                        '\n5- Você percebe vazamento de fluido de freio próximo às rodas ou sob o veículo\n'))
        if resposta in verificador:
            break
    
    match resposta:
        case 1:
            print('Seu veículo esta com ar no sistema de freios devido a sangramento inadequado')
        case 2:
            print('Seu veículo esta com pastilhas de freio desgastadas até o indicador de desgaste')
        case 3:
            print('Seu veículo esta com discos de freio empenados devido a aquecimento excessivo')
        case 4:
            print('Seu veículo esta com desgaste desigual das pastilhas de freio')
        case 5:
            print('Seu veículo esta com vazamento nos cilindros mestre ou cilindros de roda')

def suspencao_e_direcao():
    verificador = range(1,6)
    while True:
        resposta = int(input('Digite: '
                        '\n1- '
                        '\n2- '
                        '\n3- '
                        '\n4- '
                        '\n5- \n'))
        if resposta in verificador:
            break
    
    match resposta:
        case 1:
            print('')
        case 2:
            print('')
        case 3:
            print('')
        case 4:
            print('')
        case 5:
            print('')