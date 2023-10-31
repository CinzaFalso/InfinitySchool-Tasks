numero = input('Digite o número a ser multiplicado: ')
if numero.isdigit():
    #código
    numero = int(numero)
    print(f'Tabuada de {numero}:')
    for i in range(1, 11):
        print(f'{numero} X {i} = {numero * i}')
else:
    #foolproofing
    print('Você não digitou um número!, reinicie o código')