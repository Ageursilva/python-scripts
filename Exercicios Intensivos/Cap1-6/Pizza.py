#Variavel recebe o sabor das pizzas
SaborPizza=['Bacon','4 queijos','Mussarela','Carne Seca']

#Pizza do amigo

SaborAmigo=SaborPizza[:]

SaborAmigo.append('Vegetariana')

#laço for com mensagem

for Sabores in SaborPizza:
    print('Gosto de pizza de',Sabores.title(),'\n')

#saida final

print('Eua amo pizza\n')
print('Pizza é a melhor coisa do mundo\n')
print('Pizza>>>>>\n')

print('Meu amigo gosta de pizaa de',SaborAmigo)

