Pessoa_0={
    'primeiro_nome': 'Ageu',
    'ultimo_nome': 'Silva',
     'estado': 'São Paulo'
}

Pessoa_1={
    'primeiro_nome': 'João',
    'ultimo_nome': 'Goulart',
    'estado': 'Ceara'
}


Pessoa_2={
    'primeiro_nome': 'Aline',
    'ultimo_nome': 'Castro',
    'estado': 'Bahia'

}

Pessoa_3={
 'primeiro_nome': 'Josue',
 'ultimo_nome': 'Lucas',
 'estado': 'Alagoas'
}


pessoas=[Pessoa_0, Pessoa_1, Pessoa_2, Pessoa_3]

for pessoa in pessoas:
    nome_completo = f'{pessoa["primeiro_nome"]} {pessoa["ultimo_nome"]}'
    print(f"\nNome completo: {nome_completo.title()}") 

for k in pessoa.keys():
    if k == 'estado' :
         print(f'\tEstado: {pessoa[k].title()}')
