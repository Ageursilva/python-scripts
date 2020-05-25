#Variavel que vai receber os locais que desejo conhecer
Locais=[]

print('Quantas vezes você pensou em conhecer o mundo?')

print('Vamos fazer uma lista de 5 locais que você sempre sonhou em conhcer?')




#entrada de dados
Locais.append(input("Qual o primeior lugar que você quer vistar? "))

Locais.append(input("Ok, e o segundo lugar da lista? "))

Locais.append(input("Certo, o terceiro? "))

Locais.append(input("Também queria visitar todos esse locais, qual é o quarto? "))

Locais.append(input("Estamos no final, agora pense no ultimo lugar: "))

print('Então você gostária de visitar', Locais,)


#Ordem alfábética 
print('Ordem alfabetica',sorted(Locais))

print(Locais)

#Ordem alfábética reversa

print('Reversa',Locais.sort(reverse=True))

