print("Vamos fazer seu caculo de salário")

Sala_Base = int(input('Digite seu salário: '))
Bonus = int(input('Caso tenha recebido algum bônus, digite o valor: '))
Sal_bruto = Sala_Base + Bonus

if Sal_bruto < 1000:
    Imposto_R = Sal_bruto*(20/100)
else:
    Imposto_R = Sal_bruto*(15/100)
Sal_Liq = Sal_bruto - Imposto_R

print('Nese mês, seu salário vai ser de R$',Sal_Liq)
