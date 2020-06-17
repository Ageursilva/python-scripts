#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#Estou utilizando a biblioteca math para π
import math

print('Esse programa vai te ajudar a calcular a área de um círculo com base no seu raio')
#Entrada de dados

Raio = int(input('Qual o raio do círculo? '))

#Calculo
#math.pi é uma função da biblioteca "Math"
Area= math.pi*Raio**2

#saida de dados

print("A área de seu círculo é de",Area)