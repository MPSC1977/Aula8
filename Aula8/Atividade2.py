import os

os.system('cls')


def calc_multa():
    multa = excedente * MULTA
    return multa


PESO_PERMITIDO = 100
MULTA = 4

pescado = float(input('Informe o peso pescado: '))

excedente = pescado - PESO_PERMITIDO
valor_multa = calc_multa()


if pescado > PESO_PERMITIDO:
    print(f'Você excedeu o peso permitido em {excedente}Kg. Sua multa é de R${valor_multa}')
else:
    print('Não houve excedente!')