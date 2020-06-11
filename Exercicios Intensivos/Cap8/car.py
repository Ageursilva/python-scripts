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

my_new_car =  Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('Subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()