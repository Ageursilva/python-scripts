class Restaurante():
    """Essa classe simula um restaurante"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type =  cuisine_type
        self.served_client = 0
           

    def describe_restaurant(self):
        """Mostra as infomações sobre o restaurante"""
        print(f'O restaurante {self.restaurant_name.title()} é voltado para cozinha {self.cuisine_type.title()}')

    def open_restaurant(self):
        """Mostra que o restaurante ta aberto"""
        print('\nO restaurante esta aberto')

    def people_served(self):
        print(f'\nHoje o restaurante atendeu {self.served_client} pessoas hoje.')

    def number_served(self, served_client):
        self.served_client = served_client

    def increment_served(self, served_client):
        self.served_client += served_client


restaurante = Restaurante('Calango', 'Brasileira')

print(f'\nNome do restaurante: {restaurante.restaurant_name.title()}')
print(f"Tipo de cozinha: {restaurante.cuisine_type.title()}")

restaurante.describe_restaurant()

restaurante.open_restaurant()
print('--Uma hora depois')
restaurante.number_served(8)

restaurante.people_served()

