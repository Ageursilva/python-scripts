#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


print('Esse programa vai calcular o seu salário baseado no quando você recebe por hora e o tanto de horas que você trabalho no mês')

#entrada de dados

SalarioH=float(input('Quanto você recebe por hora? '))

HorasT=float(input('Quantas horas você trabalha por dia? '))

#Calculo do valor final
#Obs.: Estou supondo que todos os meses do ano tem 30 dias, em caso de meses com mais ou menos dias
# é só alterar o valor :)

Salaf= (SalarioH*HorasT)*30

#saida de dados

print('Seu salário mensal deve ser R$',Salaf)


