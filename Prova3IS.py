numero = input('Digite um número de 1 a 10 para que o código gere a tabuada: ')
if numero.isdigit() and 1 <= int(numero) <= 10:
    #código
    numero = int(numero)
    print(f'Tabuada de {numero}:')
    for i in range(1, 11):
        print(f'{numero} X {i} = {numero * i}')
else:
    #foolproofing
    print('O que voce digitou não é válido, reinicie o código!')