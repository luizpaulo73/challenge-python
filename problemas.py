with open('./problemas/problemaEletrico.txt', 'r') as arquivo:
    linha = arquivo.readlines()
    problemaEletrico = {'Bateria': linha[0],
                        'Alternador': linha[1],
                        'Motor de Arranque': linha[2],
                        'Sistema de Iluminação': linha[3],
                        'Sistemas de segurança': linha[4],
                        'Sistema de áudio e entretenimento': linha[5],
                        'Sistema de ignição': linha[6]}

with open('./problemas/problemaMecanico.txt', 'r') as arquivo:
    linha = arquivo.readlines()
    problemaMecanico = {'Motor': linha[0],
                        'Transmissão': linha[1],
                        'Suspensão e direção': linha[2],
                        'Freios': linha[3],
                        'Arrefecimento': linha[4],
                        'Correia': linha[5],
                        'Problemas de combustivel': linha[6]}
