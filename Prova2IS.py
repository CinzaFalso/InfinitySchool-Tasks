velocidade = int(input('Por favor, digite a velocidade do carro: '))

if velocidade > 80:
    print(f'O usuário do carro foi multado, a multa é: R$ {(velocidade - 80) * 20}')

# inpoot = input(': ')

# if not inpoot.isdigit():
#     print('Erro, não é um dígito')
# else:
#     inpoot = int(inpoot)
#     whatever = (inpoot - 80) * 20
#     print(whatever)