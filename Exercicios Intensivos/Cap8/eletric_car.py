class Car():
    """ Uma tentatica simples de representar um carro"""
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro"""
        self.make = make
        self.model =  model
        self.year =  year
        self.odometer_reading = 25

    def get_descriptive_name(self):
        """Devolve um nome formtado"""
        long_name = f'{str(self.year)} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print(f'This car has {str(self.odometer_reading)} miles on it')

    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor especifico
        Rejeira alteração se for uma tentativa de definir um valor menor para o hodômetro
         """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
             print("You cant't roll back an adometer!")


    def increment_odometer(self, miles):
        """Soma a quantidade especifica ao valor do hodômetro"""
        self.odometer_reading += miles


class EletricCar(Car):
    """Representa aspectos de um carro especifico de veiculos elétricos"""

    def __init__(self,make, model, year):
        """Inicializa os atriburos da classe-pai
        Em seguida, inicializa os atributos de um carro elétrico
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_baterry(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print(f"This car has a {str(self.battery_size)} -kWh baterry")

my_tesla =  EletricCar('Tesla','Model s', '2016')
print(my_tesla.get_descriptive_name ())
my_tesla.describe_baterry( )
 