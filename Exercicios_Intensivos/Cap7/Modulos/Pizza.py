def make_pizza(Tamanho,*sabores):
    print(f'\nFazemos pizzas no tamanho {str(Tamanho)} dos seguintes sabores: ')
    for sabor in sabores:
        print(f' --{sabor}')
