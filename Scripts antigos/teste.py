Sequen =  int(input('Digite o tamanho da sequência: '))

i = 0
produto = 1

while i < Sequen:
    valor = int(input('Digite um numero: '))
    i = i+1
    produto = produto * valor
print(produto)