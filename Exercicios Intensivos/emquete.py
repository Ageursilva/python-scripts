linguagem_favorita={
    'Ageu':'Python',
    'Zé':'Java',
   'Luan':'C#'
}

nomes=['Ageu','Luan',' Kener','Jean']

for nome  in  nomes:
    if nome in linguagem_favorita.keys():
        print(f'\nOlá,{nome.title()} fico feliz em saber que sua linguagem de programação favorita ')
    else:
        print(f'\nOlá,{nome.title()} que tal responder as questões? ')


