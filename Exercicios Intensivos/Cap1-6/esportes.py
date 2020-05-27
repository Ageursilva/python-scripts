#variavel para receber dados
esportes=[]

print('Quais são seus 3 esportes favoritos?')

#Entrada de dados
esportes.append(input('Digite o nome de um esporte: '))
esportes.append(input('Digite o nome de um esporte: '))
esportes.append(input('Digite o nome de um esporte: '))

print("Então seus esportes favoritos são", esportes[0],",",esportes[1],"e",esportes[2],", que legal!")


#Ordem alfabética
print('Esportes em ordem alfabética', sorted(esportes))

#Ordem alfábética reversa

print('Esportes em ordem alfabética reversa',sorted(esportes,reverse=True))

