bidu={
    'raça':'Vira-lata',
    'cor':'preto',
    'dono':'hugo'
}

bilunga={
    'raça':'dalmata',
    'cor':'branco',
    'dono':'ageu'
}

pets=[bidu,bilunga]


for  pet in pets:
    print(f'\nO cachoro do {pet["dono"].title()} é um {pet["raça"].title()} da cor {pet["cor"].title()} ')