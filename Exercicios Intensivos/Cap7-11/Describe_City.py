def Describe_city(City_Name = 'Arujá', City_County = "Brasil"):

    print(f'\nA cidade de {City_Name.title()} fica n@ {City_County.title()}')

Describe_city()

Describe_city('New York','Estados Unidos')

Describe_city(
    City_Name=input('\nQual cidade você vive? '),
    City_County=input('Em que pais fica este cidade? ')
)