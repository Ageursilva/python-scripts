def Fazer_Sanduiche(*Ingredientes):
    print('\nO sandoiche tera os seguintes ingredientes: ')
    for ingrediente in Ingredientes:
        print(f'\t{ingrediente}')

Fazer_Sanduiche('Pão de forma','Bacon')

Fazer_Sanduiche('Queijo', 'Ovos')

Fazer_Sanduiche('Tomate','Alface')
