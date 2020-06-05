def make_album(Artist_Name,Album_Name ,Quant_Faixas):
    Album = {'Artistas':Artist_Name,'Nome do album': Album_Name,'Numero de faixas': Quant_Faixas}
    return Album 
    
while True:
    print('\nDigite as informações sobre o album. ')
    print("(Para sair aperte 'q' )")

    Artist_Name = input('\nDigite o nome do cantor: ')
    if Artist_Name == 'q':
        break
    Album_Name = input('Digite o nome do album: ')
    if Album_Name == 'q':
        break
    Quant_Faixas = input('Digite o numero de faixas no album: ')
    if Quant_Faixas == 'q':
        break
    Album = make_album(Artist_Name.title(),Album_Name.title() ,Quant_Faixas)
    print(Album)