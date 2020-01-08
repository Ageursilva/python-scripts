
numero = int(input('Digite um número inteiro:'))

resto = numero % 5
resto2 = numero % 3

if resto and resto2 == 0 :
    print('FizzBuzz')
else:
    print(numero)
