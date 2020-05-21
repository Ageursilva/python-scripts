rios={
    'nilo':'egito',
    'chang Yian':'china',
    'tiete':'brasil'
}

for rio, pais in rios.items():
    print(f'\nO rio {rio.title()} fica no(a) {pais.title()}')

print('\nLista de rios: ')
for rio in rios.keys():
    print(f'\n{ rio.title()}')

print('\nLista de paises: ')
for pais in rios.values():
    print(f'\n{ pais.title()}')