contador = 0
lista = []
while True:
    numero = input('Digite um número inteiro que não seja 0, digitar zero leva o programa ao final: ')
    if numero.isdigit():
        if numero != '0':
            numero = int(numero)
            lista.append(numero)
            contador += 1
        else:
            break
    else:
        print('Digite um número inteiro!')
if len(lista) != 0:
    print(f'Foram contados {len(lista)} números, a soma total é {sum(lista)} e a média é {(sum(lista)) / len(lista)}')
else:
    print('Nenhum número foi contado, a soma e a média são nulas.')
