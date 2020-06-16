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

    def __init__(self, restaurant_name,):
      """Inicializa os atributos da classe-pai
      Em seguida, inicializa os atributos especificos de uma sorveteria
      """  
      super().__init__(restaurant_name ,cuisine_type = 'Sorveteria')
      #Mostras os sabores do s sorvetes
      self.sabores = ["Baunilha", "chocolate" ,"morango"]

    def mostrar_sabores(self)-> None :
        """ Exibe os sabores dos sorvetes"""
        print('\nSabores de sorvete: ')
        for sabor in self.sabores:
            print(f'\t{sabor.title()}')

IceCreamStand =  IceCreamStand('Bom sabor')
IceCreamStand.describe_restaurant()
IceCreamStand.open_restaurant()
IceCreamStand.mostrar_sabores()