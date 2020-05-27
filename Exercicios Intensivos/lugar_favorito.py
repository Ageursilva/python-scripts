lugares_favoritos={
    'ageu' :['casa','estadio'],

    'zé':['trabalho','quadra'],

    'kener':['baile','campo']   
}

for nome, lugares in lugares_favoritos.items():
    if len(lugares) !=1 :
        print(f'z=\nOs lugares favotios do {nome.title()} são:')
        for  lugar in lugares:
            print(f'\t{lugar.title()}')
    else:

        print(f'\nO lugar favorito de {nome.title()} é {lugares[0].title()}.')
