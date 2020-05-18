#Entrada de dados

age = int(input('Qual sua idade? '))


if age < 2:
    print("Você é um bebê!")
elif age == 2 or age<4:
    print('Você é um(a) garoto(a)!')
elif age == 4 or age < 13:
    print('Você é um(a) garoto(x)!')
elif age == 13 or  age<20:
    print("Você é um(a) adolescente!")
elif age == 20 or age < 65:
    print('Você é adulto!')
else:
    print('Você é um idoso :) ')