class Restaurante():
    """Essa classe simula um restaurante"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type =  cuisine_type
    

    def describe_restaurant(self):
        """Mostra as infomações sobre o restaurante"""
        print(f'O restaurante {self.restaurant_name.title()} é voltado para cozinha {self.cuisine_type.title()}')

    def open_restaurant(self):
        """Mostra que o restaurante ta aberto"""
        print('\nO restaurante esta aberto')


class IceCreamStand(Restaurante):
    """Representa os aspectos de uma sorveteria"""

    def __init_(self, restaurante_name, cuisine_type):
      """Inicializa os atributos da classe-pai
      Em seguida, inicializa os atributos especificos de uma sorveteria
      """  
      super().__init__(restaurant_name,cuisine_type = 'Soveteria')
      #Mostras os sabores do s sorvetes
      self.flavors = ['Baunilha', 'chocolate','Morango']

      def flavors(self):
          """ Exibe os sabores dos sorvetes"""
          print(f'\nSabores de sorvete: ')
          for flavor in flavors:
              print(f'\n{flavor.title()}')


restaurante = Restaurante('Calango', 'Brasileira')

print(f'\nNome do restaurante: {restaurante.restaurant_name.title()}')
print(f"Tipo de cozinha: {restaurante.cuisine_type.title()}")

restaurante.describe_restaurant()
restaurante.open_restaurant()

your_restaurante =  Restaurante('Sabores da Italia','Italiano')

print(f'\nNome do restaurante: {your_restaurante.restaurant_name.title()}')
print(f"Tipo de cozinha: {your_restaurante.cuisine_type.title()}")

your_restaurante.describe_restaurant()
your_restaurante.open_restaurant()


