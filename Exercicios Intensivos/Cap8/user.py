class User():
    """Essa classe simula um usuario"""
    
    def __init__(self,fist_name: str, last_name: str, user_sex: str, user_age: int, user_name: str, user_mail: str):
        '''
        Fist_name =  Primeiro nome
        Last_Name =  Ultimo nome
        User_sex =  Sexo do usuario
        User_age = Idade do usuario
        User_name =  Usuaro utlizado pare login
        user_mail =  E-mail cadastrado do usuario
        '''

        self.fist_name = fist_name.title()
        self.last_name =  last_name.title()
        self.user_sex = user_sex.upper()
        self.user_age =  user_age
        self.user_name =  user_name
        self.user_mail =  user_mail
        #nome completo
        self.full_name = f'{fist_name.title()} {last_name.title()}'
        #tentativa de llogin
        self.login_attemps = 0


    def describe_user(self):
        """ Faz um descrição do usuario"""
        print(f'\n Nome do usuario: {self.user_name}'
                    f'\nNome Completp: {self.full_name}'
                    f'\nSexo do usuario: {self.user_sex}'
                    f'\nIdade do usuario: {self.user_age}'
                    f'\nEmail do usuario: {self.user_mail}')


    def greet_user(self):
        """Mostra saudações para o usuario"""
        print(f'\nOlá {self.user_name} seja bem vindo.')

    def increment_login(self, increment_login):
        self.login_attemps += increment_login
        print(f'Houve {self.login_attemps} tentativas de login')

    def  reset_login (self, ):
        self.login_attemps = 0
        print(f'Houve {self.login_attemps} ')



user_ageu = User(
    'Ageu', 'Silva', 'M',
    21, 'Ageu_Silva', 
     'Ageu@ageu.com'
) 

user_ageu.describe_user()
user_ageu.greet_user()


user_Jose = User(
    'Jose', 'Lucas', 'M',
    23, 'Jlucas', 
     'Jose@lucas.com'
) 

user_Jose.describe_user()
user_Jose.greet_user()


user_jin = User(
    'jin', 'Suil', 'F',
    25, 'JinS13', 
     'Suil@jin.com'
) 

user_jin.describe_user()
user_jin.greet_user()
user_jin.increment_login(2)
user_jin.increment_login(4)
user_jin.reset_login()


