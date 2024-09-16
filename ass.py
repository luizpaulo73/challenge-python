tipoProblema = 0
verificador = range(1, 5)
verificador2 = range(1, 6)  # Verificador para garantir entrada válida

# Solicitando informações do carro ao usuário

def inputs():
    carroMarca = input('Digite a marca do seu carro: ')
    carroModelo = input('Digite o modelo do seu carro: ')
    return carroMarca, carroModelo

# Loop para garantir que o usuário digite uma localização válida
def localizacao():
    regioes = ['Zona Norte', 'Zona Oeste', 'Zona Leste', 'Zona Sul']
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
            return regioes[0]
        case 2:
            return regioes[1]
        case 3:
            return regioes[2]
        case 4:
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
            while True:
                resposta = int(input('Digite o número correspondente ao problema: '
                                     '\n1- Você percebeu que a luz de carga da bateria no painel de instrumentos está acesa constantemente enquanto o veículo está em funcionamento'
                                     '\n2- O veículo está com dificuldades para dar partida ou a bateria está constantemente descarregada'
                                     '\n3- Você percebeu um cheiro de queimado ou fumaça saindo do compartimento do motor'
                                     '\n4- O veículo está funcionando normalmente, mas as luzes internas ou externas estão fracas ou piscando'
                                     '\n5- Você notou algum ruído estranho vindo do compartimento do motor, especialmente próximo ao alternador\n'))
                if resposta in verificador2:
                    break
                else:
                    print('Digite um valor válido!')

                # Correspondência da resposta do usuário com mensagens informativas sobre o problema com o alternador
            match resposta:
                case 1:
                    print(
                        'Seu veículo está com falha no alternador em fornecer energia suficiente para carregar a bateria')
                    precos = [557.55, 932.48, 855.95, 900.22, 693.39]
                case 2:
                    print(
                        'Seu veículo está com falha no alternador em recarregar a bateria adequadamente durante a operação do veículo')
                    precos = [557.55, 932.48, 855.95, 900.22, 693.39]
                case 3:
                    print('Seu veículo está com sobrecarga do alternador')
                    precos = [557.55, 932.48, 855.95, 900.22, 693.39]
                case 4:
                    print(
                        'Seu veículo está com alternador fornecendo voltagem inadequada')
                    precos = [144.90, 47.84, 139.90, 119, 158.06]
                case 5:
                    print('Seu veículo está com rolamentos do alternador desgastados')
                    precos = [63.90, 131.90, 99.90, 127.79, 57.21]
            return precos

        case 2:
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
                    precos = [479, 162.90, 548, 651.90, 470.44]
                case 2:
                    print('Seu veículo está com falha no motor de arranque')
                    precos = [479, 162.90, 548, 651.90, 470.44]
                case 3:
                    print(
                        'Seu veículo está com problemas de combustível (falta de combustível ou problemas no sistema de injeção)')
                    precos = [74.90, 99.23, 125, 185.86, 174.90]
                case 4:
                    print(
                        'Seu veículo está com sobrecarga elétrica no motor de arranque')
                    precos = [557.55, 932.48, 855.95, 900.22, 693.39]
            return precos

        case 3:
            # Loop para solicitar ao usuário que selecione o problema com o sistema de iluminação até que uma resposta válida seja fornecida
            while True:
                resposta = int(input('Digite o número correspondente ao problema: '
                                     '\n1- Você notou que uma ou mais lâmpadas do veículo não estão funcionando corretamente'
                                     '\n2- Você percebeu que as luzes do painel de instrumentos estão fracas ou piscando'
                                     '\n3- As luzes do farol estão fracas ou oscilando enquanto o veículo está em movimento'
                                     '\n4- Você percebeu que os faróis estão embaçados ou com condensação interna\n'))
                if resposta in verificador:
                    break
                else:
                    print('Digite um valor válido!')

            # Correspondência da resposta do usuário com mensagens informativas sobre o problema com o sistema de iluminação
            match resposta:
                case 1:
                    print('Seu veículo está com lâmpadas queimadas')
                    precos = [33.90, 38.75, 71.01, 39.52, 45.90]
                case 2:
                    print('Seu veículo está com problemas no regulador de voltagem')
                    precos = [251.75, 219.90, 284.05, 281, 160.54]
                case 3:
                    print('Seu veículo está com alternador com voltagem irregular')
                    precos = [557.55, 932.48, 855.95, 900.22, 693.39]
                case 4:
                    print(
                        'Seu veículo está com entrada de umidade nos faróis devido a vedação defeituosa')
                    precos = [82.76, 199.90, 69, 79.80, 41.80]
            return precos
        case 4:
            # Loop para solicitar ao usuário que selecione o problema com o sistema de ignição até que uma resposta válida seja fornecida
            while True:
                resposta = int(input('Digite o número correspondente ao problema: '
                                     '\n1- O veículo está tendo dificuldades para ligar ou não liga de todo'
                                     '\n2- Você percebeu que o motor está falhando ou perdendo potência durante a condução'
                                     '\n3- Você notou que o motor está superaquecendo ou funcionando irregularmente em marcha lenta'
                                     '\n4- Você ouviu algum ruído de cliques ao tentar ligar o veículo'
                                     '\n5- Você percebeu algum cheiro de combustível não queimado saindo do escapamento\n'))
                if resposta in verificador2:
                    break
                else:
                    print('Digite um valor válido!')

            # Correspondência da resposta do usuário com mensagens informativas sobre o problema com o sistema de ignição
            match resposta:
                case 1:
                    print('Seu veículo está com problemas nas velas de ignição')
                    precos = [141.70, 218.90, 208.23, 124.99, 95.04]
                case 2:
                    print('Seu veículo está com cabos de vela danificados')
                    precos = [141.70, 218.90, 208.23, 124.99, 95.04]
                case 3:
                    print(
                        'Seu veículo está com problemas com o sensor de temperatura do motor')
                    precos = [42, 30.90, 69.76, 34.50, 34.99]
                case 4:
                    print('Seu veículo está com problemas com o relé de partida')
                    precos = [34.69, 53.99, 75.30, 41.29, 71.90]
                case 5:
                    print(
                        'Seu veículo está com problemas de ignição que resultam em combustão incompleta')
                    precos = [141.70, 218.90, 208.23, 124.99, 95.04]
            return precos


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
            # Loop para solicitar ao usuário que selecione o problema do motor até que uma resposta válida seja fornecida
            while True:
                resposta = int(input('Digite o número correspondente ao problema: '
                                     '\n1- Se o motor está fazendo algum barulho incomum'
                                     '\n2- Se o veículo está tendo dificuldades para ligar'
                                     '\n3- Se o motor está perdendo potência'
                                     '\n4- Se há vazamentos visíveis de fluidos do motor\n'))
                if resposta in verificador:
                    break
                else:
                    print('Digite um valor válido!')

            # Correspondência da resposta do usuário com mensagens informativas sobre o problema do motor
            match resposta:
                case 1:
                    print('A correia dentada do seu veículo está com perda de tensão')
                    precos = [595.85, 789.90, 395.00, 279.90, 542.99]
                case 2:
                    print('As velas de ignição do seu veículo estão gastas')
                    precos = [141.70, 218.90, 208.23, 124.99, 95.04]
                case 3:
                    print('O sistema de combustível está com problemas')
                    precos = [185.96, 99.23, 125, 174.90, 217.80]
                case 4:
                    print('Seu veículo está com vazamento de óleo do cárter')
                    precos = [78.99, 132.90, 109.90, 65.78, 144.16]

        case 2:
            # Loop para solicitar ao usuário que selecione o problema da transmissão até que uma resposta válida seja fornecida
            while True:
                resposta = int(input('Digite o número correspondente ao problema: '
                                     '\n1- Se o pedal da embreagem está ficando preso ou afundando facilmente'
                                     '\n2- Se você percebe um cheiro de queimado ao dirigir'
                                     '\n3- Se o veículo está tendo dificuldades para engatar as marchas'
                                     '\n4- Se você nota trepidação ou vibração ao soltar a embreagem'
                                     '\n5- Se o veículo está se movendo mesmo com o pedal da embreagem totalmente pressionado\n'))
                if resposta in verificador2:
                    break
                else:
                    print('Digite um valor válido!')

            # Correspondência da resposta do usuário com mensagens informativas sobre o problema da transmissão
            match resposta:
                case 1:
                    print(
                        'Seu veículo está com o cabo de embreagem desgastado ou danificado')
                    precos = [454.41, 319.99, 333, 158, 225.15]
                case 2:
                    print(
                        'Seu veículo está com desgaste excessivo do disco da embreagem')
                    precos = [546.26, 301.41, 599.99, 403.37, 232.05]
                case 3:
                    print(
                        'Seu veículo está com desgaste do disco ou platô da embreagem')
                    precos = [546.26, 301.41, 599.99, 403.37, 232.05]
                case 4:
                    print('Seu veículo está com disco da embreagem empenado')
                    precos = [546.26, 301.41, 599.99, 403.37, 232.05]
                case 5:
                    print(
                        'Seu veículo está com vazamento de fluido hidráulico da embreagem')
                    precos = [148.41, 178, 133.94, 103, 124.26]

        case 3:
            while True:
                resposta = int(input('Digite o número correspondente ao problema: '
                                     '\n1- Você sente vibrações excessivas no volante ao dirigir em alta velocidade'
                                     '\n2- O veículo está inclinando ou puxando para um lado ao fazer curvas'
                                     '\n3- Você ouve ruídos de batidas ou rangidos ao passar por solavancos ou irregularidades na estrada'
                                     '\n4- O volante está difícil de girar ou há folga excessiva na direção'))
                if resposta in verificador:
                    break
                else:
                    print('Digite um valor válido!')

                # Correspondência da resposta do usuário com mensagens informativas sobre o problema de suspensão e direção
            match resposta:
                case 1:
                    print('Seu veículo está com desgaste ou desalinhamento dos pneus')
                    precos = [150, 200, 300, 100]
                case 2:
                    print(
                        'Seu veículo está com os amortecedores desgastados ou com vazamento')
                    precos = [530.99, 999.99, 599.99, 450.45, 479.90]
                case 3:
                    print('Seu veículo está com as buchas da suspensão desgastadas')
                    precos = [177.19, 153, 140.60, 289.90, 165.90]
                case 4:
                    print(
                        'Seu veículo está com baixo nível de fluido de direção hidráulica')
                    precos = [130.65, 309.57, 278.57, 200.99, 199.90]

        case 4:
            while True:
                resposta = int(input('Digite o número correspondente ao problema: '
                                     '\n1- Você nota que o pedal do freio está afundando até o fundo ou parece esponjoso'
                                     '\n2- Você ouve um ruído agudo ou rangido ao frear'
                                     '\n3- Você sente vibração no volante ou no pedal do freio ao frear em alta velocidade'
                                     '\n4- O veículo está puxando para um lado ao frear'
                                     '\n5- Você percebe vazamento de fluido de freio próximo às rodas ou sob o veículo\n'))
                if resposta in verificador2:
                    break
                else:
                    print('Digite um valor válido!')

                # Correspondência da resposta do usuário com mensagens informativas sobre o problema nos freios
            match resposta:
                case 1:
                    print(
                        'Seu veículo está com ar no sistema de freios devido a sangramento inadequado')
                    precos = [120, 400, 175.99, 154.66, 309.99]
                case 2:
                    print(
                        'Seu veículo está com pastilhas de freio desgastadas até o indicador de desgaste')
                    precos = [136, 454.03, 418.40, 253.90, 171.90]
                case 3:
                    print(
                        'Seu veículo está com discos de freio empenados devido a aquecimento excessivo')
                    precos = [297, 569.05, 268.90, 380.34, 337.90]
                case 4:
                    print(
                        'Seu veículo está com desgaste desigual das pastilhas de freio')
                    precos = [150, 200, 300, 100]
                case 5:
                    print(
                        'Seu veículo está com vazamento nos cilindros mestre ou cilindros de roda')
                    precos = [181.41, 179, 368.10, 213.75, 216.27]
    return precos

def preco(precos):
    # definindo maior preço
    maior_preco = precos[0]
    for preco in precos:
        if preco > maior_preco:
            maior_preco = preco

# definindo menor preço
    menor_preco = precos[0]
    for preco in precos:
        if preco < menor_preco:
            menor_preco = preco

# media dos precos
    i = 0
    soma = 0
    for preco in range(len(precos)):
        soma += precos[i]
        i += 1
    media = soma / len(precos)

    return maior_preco, menor_preco, media

def info_usuario(problema):
    return {
        "nome": input("Nome: "),
        "cpf": input("CPF: "),
        "telefone": input("Telefone: "),
        "email": input("E-mail: "),
        "carro": {
            "marca": input("Marca do carro: "),
            "modelo": input("Modelo: "),
            "ano": int(input("Ano: ")),
            "problema": problema
        }
    }

# Lista para armazenar os registros
banco_de_dados = []

def criar():
    problema = eletrico_mecanico(0) 
    banco_de_dados.append(info_usuario(problema))
    print("Registro adicionado!")

def ler():
    contador = 1
    for registro in banco_de_dados:
        print(f"{contador} - {registro}")
        contador += 1

def atualizar():
    cpf = input("CPF do usuário a atualizar: ")
    for registro in banco_de_dados:
        if registro["cpf"] == cpf:
            print("Atualizando registro...")
            problema = eletrico_mecanico(0) 
            banco_de_dados[banco_de_dados.index(registro)] = info_usuario(problema)
            print("Registro atualizado!")
            return
        else:
            print("Registro não encontrado!")

def deletar():
    cpf = input("CPF do usuário a deletar: ")
    for registro in banco_de_dados:
        if registro["cpf"] == cpf:
            banco_de_dados.remove(registro)
            print("Registro deletado!")
            return
        else:
            print("Registro não encontrado!")

def processar_dados():
    regiao = localizacao()
    tipoProblema = eletrico_mecanico(0) 
    if tipoProblema == 1:
        precos = eletrico()
    elif tipoProblema == 2:
        precos = mecanico()
    maior_preco, menor_preco, media = preco(precos)
    print(f'Problema detectado! \nTraga seu carro para alguma oficina credenciada da Porto Seguro na {regiao}'
          f'\nO valor médio das peças para consertar seu veículo é de: R${media:.2f}'
          f'\nPodendo variar de R${menor_preco:.2f} até R${maior_preco:.2f}')

def menu():
    while True:
        print("\n1. Criar\n2. Ler\n3. Atualizar\n4. Deletar\n5. Detectar Problemas\n6. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            criar()
        elif opcao == "2":
            ler()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            processar_dados()
        elif opcao == "6":
            break
        else:
            print("Opção inválida, tente novamente.")

# ==================== #
#       PRINCIPAL      #
# ==================== #
menu()
