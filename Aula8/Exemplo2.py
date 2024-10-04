import os

os.system('cls')

import random

# num = random.randint(1, 25)

def sorteio(v1, v2, v3):
    
    return [random.randint(inicio, final) for _ in range(qtde)]


inicio = int(input('Informe o primeiro valor: '))
final = int(input('Informe o final: '))
qtde = int(input('Quantos números você quer gerar? '))

sorteados = sorteio(inicio, final, qtde)

print(sorteados)