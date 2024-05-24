def motor():
    # Definindo um intervalo de verificação para garantir que a resposta do usuário seja válida
    verificador = range(1, 6)
    
    # Loop para solicitar ao usuário que selecione o problema do motor até que uma resposta válida seja fornecida
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
    
    # Correspondência da resposta do usuário com mensagens informativas sobre o problema do motor
    match resposta:
        case 1:
            print('A correia dentada do seu veículo está com perda de tensão')
            precos = [595.85 , 789.90 , 395.00 , 279.90 , 542.99]
        case 2:
            print('Seu veículo está queimando óleo devido a vazamentos ou desgaste de peças internas')
            precos = []
        case 3:
            print('As velas de ignição do seu veículo estão gastas')
            precos = [141.70 , 218.90 , 208.23 , 124.99 , 95.04]
        case 4:
            print('O sistema de combustível está com problemas')
            precos = []
        case 5:
            print('Seu veículo está com vazamento de óleo do cárter')
            precos = []
    return precos

# ja foi
def transmissao():
    # Definindo um intervalo de verificação para garantir que a resposta do usuário seja válida
    verificador = range(1, 6)
    
    # Loop para solicitar ao usuário que selecione o problema da transmissão até que uma resposta válida seja fornecida
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
    
    # Correspondência da resposta do usuário com mensagens informativas sobre o problema da transmissão
    match resposta:
        case 1:
            print('Seu veículo está com o cabo de embreagem desgastado ou danificado')
            precos = [454.41 , 319.99 , 333 , 158 , 225.15]
        case 2:
            print('Seu veículo está com desgaste excessivo do disco da embreagem')
            precos = [546.26 , 301.41 , 599.99 , 403.37 , 232.05]
        case 3:
            print('Seu veículo está com desgaste do disco ou platô da embreagem')
            precos = [546.26 , 301.41 , 599.99 , 403.37 , 232.05]
        case 4:
            print('Seu veículo está com disco da embreagem empenado')
            precos = [546.26 , 301.41 , 599.99 , 403.37 , 232.05]
        case 5:
            print('Seu veículo está com vazamento de fluido hidráulico da embreagem')
            precos = [148.41 , 178 , 133.94 , 103 , 124.26]
    return precos

def suspencao_e_direcao():
    # Definindo um intervalo de verificação para garantir que a resposta do usuário seja válida
    verificador = range(1, 6)
    
    # Loop para solicitar ao usuário que selecione o problema de suspensão e direção até que uma resposta válida seja fornecida
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

    # Correspondência da resposta do usuário com mensagens informativas sobre o problema de suspensão e direção
    match resposta:
        case 1:
            print('Seu veículo está com desgaste ou desalinhamento dos pneus')
            precos = [150 , 200 , 300 , 100]
        case 2:
            print('Seu veículo está com os amortecedores desgastados ou com vazamento')
            precos = [530.99 , 999.99 , 599.99 , 450.45 , 479.90]
        case 3:
            print('Seu veículo está com as buchas da suspensão desgastadas')
            precos = [177.19 , 153 , 140.60 , 289.90 , 165.90]
        case 4:
            print('Seu veículo está com baixo nível de fluido de direção hidráulica')
            precos = []
        case 5:
            print('Seu veículo está com vazamento de fluido de direção hidráulica')
            precos = []
    return precos

def freios():
    # Definindo um intervalo de verificação para garantir que a resposta do usuário seja válida
    verificador = range(1, 6)
    
    # Loop para solicitar ao usuário que selecione o problema de freios até que uma resposta válida seja fornecida
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

    # Correspondência da resposta do usuário com mensagens informativas sobre o problema nos freios
    match resposta:
        case 1:
            print('Seu veículo está com ar no sistema de freios devido a sangramento inadequado')
            precos = []
        case 2:
            print('Seu veículo está com pastilhas de freio desgastadas até o indicador de desgaste')
            precos = [136 , 454.03 , 418.40 , 253.90 , 171.90]
        case 3:
            print('Seu veículo está com discos de freio empenados devido a aquecimento excessivo')
            precos = []
        case 4:
            print('Seu veículo está com desgaste desigual das pastilhas de freio')
            precos = [150 , 200 , 300 , 100]
        case 5:
            print('Seu veículo está com vazamento nos cilindros mestre ou cilindros de roda')
            precos = []
    return precos

def alternador():
    # Definindo um intervalo de verificação para garantir que a resposta do usuário seja válida
    verificador = range(1, 6)
    
    # Loop para solicitar ao usuário que selecione o problema com o alternador até que uma resposta válida seja fornecida
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

    # Correspondência da resposta do usuário com mensagens informativas sobre o problema com o alternador
    match resposta:
        case 1:
            print('Seu veículo está com falha no alternador em fornecer energia suficiente para carregar a bateria')
            precos = []
        case 2:
            print('Seu veículo está com falha no alternador em recarregar a bateria adequadamente durante a operação do veículo')
            precos = []
        case 3:
            print('Seu veículo está com sobrecarga do alternador')
            precos = []
        case 4:
            print('Seu veículo está com alternador fornecendo voltagem inadequada')
            precos = []
        case 5:
            print('Seu veículo está com rolamentos do alternador desgastados')
            precos = []
    return precos

def motorArranque():
    # Definindo um intervalo de verificação para garantir que a resposta do usuário seja válida
    verificador = range(1, 6)
    
    # Loop para solicitar ao usuário que selecione o problema com o motor de arranque até que uma resposta válida seja fornecida
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

    # Correspondência da resposta do usuário com mensagens informativas sobre o problema com o motor de arranque
    match resposta:
        case 1:
            print('Seu veículo está com falha no motor de arranque')
            precos = []
        case 2:
            print('Seu veículo está com solenóide defeituoso no motor de arranque')
            precos = []
        case 3:
            print('Seu veículo está com problemas de combustível (falta de combustível ou problemas no sistema de injeção)')
            precos = []
        case 4:
            print('Seu veículo está com sobrecarga elétrica no motor de arranque')
            precos = []
    return precos

def sistemaIluminacao():
    # Definindo um intervalo de verificação para garantir que a resposta do usuário seja válida
    verificador = range(1, 6)
    
    # Loop para solicitar ao usuário que selecione o problema com o sistema de iluminação até que uma resposta válida seja fornecida
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

    # Correspondência da resposta do usuário com mensagens informativas sobre o problema com o sistema de iluminação
    match resposta:
        case 1:
            print('Seu veículo está com lâmpadas queimadas, fusíveis queimados')
            precos = []
        case 2:
            print('Seu veículo está com problemas no regulador de voltagem')
            precos = []
        case 3:
            print('Seu veículo está com alternador com voltagem irregular')
            precos = []
        case 4:
            print('Seu veículo está com faróis desalinhados devido a impactos')
            precos = []
        case 5:
            print('Seu veículo está com entrada de umidade nos faróis devido a vedação defeituosa')
            precos = []
    return precos

def sistemaIgnicao():
    # Definindo um intervalo de verificação para garantir que a resposta do usuário seja válida
    verificador = range(1, 6)
    
    # Loop para solicitar ao usuário que selecione o problema com o sistema de ignição até que uma resposta válida seja fornecida
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

    # Correspondência da resposta do usuário com mensagens informativas sobre o problema com o sistema de ignição
    match resposta:
        case 1:
            print('Seu veículo está com problemas nas velas de ignição')
            precos = [141.70 , 218.90 , 208.23 , 124.99 , 95.04]
        case 2:
            print('Seu veículo está com cabos de vela danificados')
            precos = []
        case 3:
            print('Seu veículo está com problemas com o sensor de temperatura do motor')
            precos = []
        case 4:
            print('Seu veículo está com problemas com o relé de partida')
            precos = []
        case 5:
            print('Seu veículo está com problemas de ignição que resultam em combustão incompleta')
            precos = []
    return precos