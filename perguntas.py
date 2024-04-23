def motor():
    verificador = range(1, 6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                             '\n1- Se o motor está fazendo algum barulho incomum'
                             '\n2- Se alguma fumaça está saindo do motor'
                             '\n3- Se o veículo está tendo dificuldades para ligar'
                             '\n4- Se o motor está perdendo potência'
                             '\n5- Se há vazamentos visíveis de fluidos do motor\n'))
        if resposta in verificador:
            break
        else:
            print('Digite um valor válido!')

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
    verificador = range(1, 6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                             '\n1- Se o pedal da embreagem está ficando preso ou afundando facilmente'
                             '\n2- Se você percebe um cheiro de queimado ao dirigir'
                             '\n3- Se o veículo está tendo dificuldades para engatar as marchas'
                             '\n4- Se você nota trepidação ou vibração ao soltar a embreagem'
                             '\n5- Se o veículo está se movendo mesmo com o pedal da embreagem totalmente pressionado\n'))
        if resposta in verificador:
            break
        else:
            print('Digite um valor válido!')

    match resposta:
        case 1:
            print('Seu veículo esta com o cabo de embreagem desgastado ou danificado')
        case 2:
            print('Seu veículo esta com desgaste excessivo do disco da embreagem')
        case 3:
            print('Seu veículo esta com desgaste do disco ou platô da embreagem')
        case 4:
            print('Seu veículo esta com disco da embreagem empenado')
        case 5:
            print('Seu veículo esta com vazamento de fluido hidráulico da embreagem')

def suspencao_e_direcao():
    verificador = range(1, 6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                             '\n1- Você sente vibrações excessivas no volante ao dirigir em alta velocidade'
                             '\n2- O veículo está inclinando ou puxando para um lado ao fazer curvas'
                             '\n3- Você ouve ruídos de batidas ou rangidos ao passar por solavancos ou irregularidades na estrada'
                             '\n4- O volante está difícil de girar ou há folga excessiva na direção'
                             '\n5- Você nota vazamentos de fluido sob o veículo próximo às rodas dianteiras\n'))
        if resposta in verificador:
            break
        else:
            print('Digite um valor válido!')

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
    verificador = range(1, 6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                             '\n1- Você nota que o pedal do freio está afundando até o fundo ou parece esponjoso'
                             '\n2- Você ouve um ruído agudo ou rangido ao frear'
                             '\n3- Você sente vibração no volante ou no pedal do freio ao frear em alta velocidade'
                             '\n4- O veículo está puxando para um lado ao frear'
                             '\n5- Você percebe vazamento de fluido de freio próximo às rodas ou sob o veículo\n'))
        if resposta in verificador:
            break
        else:
            print('Digite um valor válido!')

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

def alternador():
    verificador = range(1, 6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                             '\n1- Você percebeu que a luz de carga da bateria no painel de instrumentos está acesa constantemente enquanto o veículo está em funcionamento'
                             '\n2- O veículo está com dificuldades para dar partida ou a bateria está constantemente descarregada'
                             '\n3- Você percebeu um cheiro de queimado ou fumaça saindo do compartimento do motor'
                             '\n4- O veículo está funcionando normalmente, mas as luzes internas ou externas estão fracas ou piscando'
                             '\n5- Você notou algum ruído estranho vindo do compartimento do motor, especialmente próximo ao alternador\n'))
        if resposta in verificador:
            break
        else:
            print('Digite um valor válido!')

    match resposta:
        case 1:
            print('Seu veículo esta com falha no alternador em fornecer energia suficiente para carregar a bateria')
        case 2:
            print('Seu veículo esta com falha no alternador em recarregar a bateria adequadamente durante a operação do veículo')
        case 3:
            print('Seu veículo esta com sobrecarga do alternador')
        case 4:
            print('Seu veículo esta com alternador fornecendo voltagem inadequada')
        case 5:
            print('Seu veículo esta com rolamentos do alternador desgastados')

def motorArranque():
    verificador = range(1, 6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                             '\n1- O motor de arranque não está girando quando você vira a chave para a posição de partida'
                             '\n2- Você ouve um ruído de cliques ao tentar dar partida no veículo'
                             '\n3- O motor de arranque está girando, mas o motor do veículo não está ligando'
                             '\n4- Você percebeu algum cheiro de queimado vindo do compartimento do motor ao tentar dar partida no veículo'))
        if resposta in verificador:
            break
        else:
            print('Digite um valor válido!')

    match resposta:
        case 1:
            print('Seu veículo esta com falha no motor de arranque')
        case 2:
            print('Seu veículo esta com solenóide defeituoso no motor de arranque')
        case 3:
            print('Seu veículo esta com problemas de combustível (falta de combustível ou problemas no sistema de injeção)')
        case 4:
            print('Seu veículo esta com sobrecarga elétrica no motor de arranque')

def sistemaIluminacao():
    verificador = range(1, 6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                             '\n1- Você notou que uma ou mais lâmpadas do veículo não estão funcionando corretamente'
                             '\n2- Você percebeu que as luzes do painel de instrumentos estão fracas ou piscando'
                             '\n3- As luzes do farol estão fracas ou oscilando enquanto o veículo está em movimento'
                             '\n4- Você notou que os faróis estão desalinhados ou apontando para baixo'
                             '\n5- Você percebeu que os faróis estão embaçados ou com condensação interna\n'))
        if resposta in verificador:
            break
        else:
            print('Digite um valor válido!')

    match resposta:
        case 1:
            print('Seu veículo esta com lâmpadas queimadas, fusíveis queimados')
        case 2:
            print('Seu veículo esta com problemas no regulador de voltagem')
        case 3:
            print('Seu veículo esta com alternador com voltagem irregular')
        case 4:
            print('Seu veículo esta com faróis desalinhados devido a impactos')
        case 5:
            print('Seu veículo esta com entrada de umidade nos faróis devido a vedação defeituosa')

def sistemaIgnicao():
    verificador = range(1, 6)
    while True:
        resposta = int(input('Digite o número correspondente ao problema: '
                             '\n1- O veículo está tendo dificuldades para ligar ou não liga de todo'
                             '\n2- Você percebeu que o motor está falhando ou perdendo potência durante a condução'
                             '\n3- Você notou que o motor está superaquecendo ou funcionando irregularmente em marcha lenta'
                             '\n4- Você ouviu algum ruído de cliques ao tentar ligar o veículo'
                             '\n5- Você percebeu algum cheiro de combustível não queimado saindo do escapamento\n'))
        if resposta in verificador:
            break
        else:
            print('Digite um valor válido!')

    match resposta:
        case 1:
            print('Seu veículo esta com problemas nas velas de ignição')
        case 2:
            print('Seu veículo esta com cabos de vela danificados')
        case 3:
            print('Seu veículo esta com problemas com o sensor de temperatura do motor')
        case 4:
            print('Seu veículo esta com problemas com o relé de partida')
        case 5:
            print('Seu veículo esta com problemas de ignição que resultam em combustão incompleta')