import os

import random

def limpa_tela():
    os.system('cls')


def decoracao():
    print(12*'=')


def gerar_numeros():
    x = random.randint(1, 50)
    y = random.randint(1, 100)
    return x, y


def adi(x, y):
    res_adi = x + y
    return res_adi


def sub(x, y):
    res_sub = x - y
    return res_sub


def mult(x, y):
    res_mult = x * y
    return res_mult


def div(x, y):
    res_div = x / y
    return float(res_div)


limpa_tela()
decoracao()
print('CALCULADORA')

x, y = gerar_numeros()

res_adi = adi(x, y)
print(f'Os números sorteados foram {x} e {y}. A soma deles é igual a {res_adi}')

res_sub = sub(x, y)
print(f'Os números sorteados foram {x} e {y}. A subtração entre eles é igual a {res_sub}')

res_mult = mult(x, y)
print(f'Os números sorteados foram {x} e {y}. A multiplicação entre eles é igual a {res_mult}')

res_div = div(x, y)
print(f'Os números sorteados foram {x} e {y}. A divisão entre eles é igual a {res_div}')