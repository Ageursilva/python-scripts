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

class Battery():
    """""Uma tentativa de modelar uma bateria para um carro eletrico"""
    def __init__(self, battery_size =70):
        """"Inicializa os atriburos da bateria"""
        self.battery_size =  battery_size
        
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print(f"This car has a {str(self.battery_size)} -kWh baterry")
    
    def get_range(self):
        """Exibe uma frase sobre a distãncia que o carro é capaz de percorrer com essa bateria"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f'This car can go approximately {str(range)} milles on full charge'
        print(message)


class EletricCar(Car):
    """Representa aspectos de um carro especifico de veiculos elétricos"""

    def __init__(self,make, model, year):
        """Inicializa os atriburos da classe-pai
        Em seguida, inicializa os atributos de um carro elétrico
        """
        super().__init__(make, model, year)
        self.battery =  Battery()
   

my_tesla =  EletricCar('Tesla','Model s', '2016')

print(my_tesla.get_descriptive_name ())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
 