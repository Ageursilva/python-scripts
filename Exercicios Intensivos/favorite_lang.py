Linguagem_Favorita = {
'Jen': ['Python','Java','Ruby'],
'Lucas': ['Cobol'],
'Jubileu':['Python','Java','Ruby','Cobol']
}

for nome,linguas in Linguagem_Favorita.items():
    if len(linguas) > 1:
        print(f'\n {nome.title()} suas linguagens favoritas são:')
        for lingua in linguas:
            print(f'\t {lingua.title()}')
    else:
        for lingua in linguas:
            print(f'\n {nome.title()} suas linguagem favorita  é {lingua.title()}')