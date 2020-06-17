Pedidos_Lanches = ['bacon', 'Calabresa','Peixe','Frango', 'Queijo','Frango','Frango']

Lanches_Finalizados = [ ]

while 'Frango' in Pedidos_Lanches:
    Pedidos_Lanches.remove('Frango')
 
while  Pedidos_Lanches:
    Peditos_Feitos = Pedidos_Lanches.pop()
    
    print(f"\nPreparei seu lanche de {Peditos_Feitos.title()}")
    Lanches_Finalizados.append(Peditos_Feitos)

for finalizados in Lanches_Finalizados:
    print('\nLista de pedidos finalizados' )
    print(f"\t{finalizados}")
