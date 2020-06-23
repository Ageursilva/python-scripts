import json

#Carrega o nome do usuario se foi armazenado anteriormente
#Caso contrário, pede que o usuario forneça o nome e armaneza essa informação
def get_stored_username():
    """Obtém o nome do usuario já armazeanado se estiver disponivvel. """
    try:
        filename = 'username.json'
        with open(filename) as f_obj:
            username= json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_new_username():
    """ Pede um novo nome de usuario """
    username = input('What is your name? ')
    filename =  'username.json'
    with open(filename,'w') as f_obj:
         json.dump(username,f_obj)
    return username


def greet_user():
    """ Saúda o usúario pelo nome. """
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}")
    else:
        username = get_stored_username()
         print(f"We'll remember your when you come back, {username}")
   
greet_user()