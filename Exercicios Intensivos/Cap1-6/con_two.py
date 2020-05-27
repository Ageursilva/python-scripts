#Faça um Programa que peça dois números e imprima o maior deles

print('Os numeros digitados devem ser diferentes')

#Essa variavel recebe o primeiro valor digitado

Pvalor=[]
Pvalor.append(int(input('Digite o primeiro valor: ')))

#Essa variavel recece o segundo valor dogitado

Svalor=[]
Svalor.append(int(input('Digite o segundo valor: ')))

if Pvalor > Svalor:
    print('\nO primeiro valor digitado é maior:',Pvalor)
elif Pvalor < Svalor:
   print('\nO segundo valor é maior:',Svalor )
elif Pvalor == Svalor:
    print('\nOs valore são iguais')