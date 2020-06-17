def Info_Car(Fabricante: str, Modelo: str, **Info_Extra):

    Carro = dict()

    Carro['Fabricante'] = Fabricante
    Carro['Modelo'] = Modelo

    for key, value in Info_Extra.items():
        Carro[key] = value

    return Carro

Carro_Dict = Info_Car('Ferrari',  'F8',Cor = 'Vermelha',Ano = '2019')

print(Carro_Dict) 

