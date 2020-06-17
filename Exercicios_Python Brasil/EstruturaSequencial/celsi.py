#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

print('Esse programa vai conveter ºF para ºC')

#entrada de dados

Faren=float(input("Digite o valo que deseja converter: "))

#Conversaõ
Celsi = (5 * (Faren-32) / 9)

#saida de dados

print("O valor é",Celsi,"ºc")