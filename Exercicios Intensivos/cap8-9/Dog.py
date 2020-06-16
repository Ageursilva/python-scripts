class Dog():
    """ Uma tentativa de modelar um cahorro """
    def __init__(self, name, age):
         """Inicia os atributos name e age"""
         self.name = name
         self.age = age

    
    def sit(self):
         """Simula um cachorro sentanto em reposta a um comando"""
         print(f'{self.name.title()} estas sentado')
            
    
    def roll_over(self):
        """Simula o chachorro rolando"""
        print(f'{self.name.title()} esta rolando')
        
my_dog = Dog('Willie', 6  )
your_dog = Dog('Lucy', 3 )

print(f"\n My dog's name is {my_dog.name.title()} .")
print(f"My dog is {str(my_dog.age)} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name.title()} .")
print(f"Your dog is {str(your_dog.age)} years old")
your_dog.sit()