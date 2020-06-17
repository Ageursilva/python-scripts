import math
#Entrada de dados

ValorA = float(input('Digite o valor de A:'))
ValorB = float(input('Digite o valor de B:'))
ValorC = float(input('Digite o valor de C:'))

#Conversão para delta
#Não funcionar com ()

Delta = ValorB**2-4*ValorA*ValorC
DeltaC= math.sqrt(Delta)

#Calcula as duas raizes reais
if Delta > 0: 

    X1 = (-ValorB + DeltaC)/(2*ValorA)
    X2 = (-ValorB - DeltaC)/(2*ValorA)
    print('A primeira raiz é:',X1)
    print('A segunda raiz é:',X2) 

#Não faz conta, pois vai dar numero iracional
if Delta < 0: 

   print('Seu delta é menor que 0')
   print('Essa equação não possuie raiz real')

#Delta == 0
#As duas raizes devem ser iguais
elif Delta == 0:
    X1 = (-ValorB + DeltaC)/(2*ValorA)
    X2 = (-ValorB - DeltaC)/(2*ValorA)
    print('Seu delta é igual a 0')
    print('As raizes são iguais sendo X1=',X1,'e X2=',X2)
    


