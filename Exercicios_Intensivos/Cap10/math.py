print('Esse programa vai fazer a soma de dois numeros!')
print('Presione "Q" para sair.')

while True:
    first_number = input('\nDigite um numero: ')
    if first_number == "q":
        break
    second_number = input('Digite outro numero: ')
    try:
        awser = int(first_number) + int( second_number)
    except ValueError:
        print('Por favor, digite apenas numeros. ')
    else:
        print(f'A soma de {first_number} + {second_number} é =  {awser}')