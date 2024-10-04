import os

os.system('cls')


def calcula_dobro_triplo(x):
    dobro = x * 2
    triplo = x * 3
    return dobro, triplo


num = float(input('Informe o número: '))

x2, x3 = calcula_dobro_triplo(num)

print(f'O dobro do seu número é {x2} e o triplo é {x3}')
