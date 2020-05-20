
current_user = ['Ageu','Luan','Zé','Vitor','Kener','Mauricio']
new_user = ['Federado','Luan','Ageu','Lucas']


for  users in new_user:
    if  users  in  current_user:
        print(f'O usuario:{users} já esta sendo usado, por favor, faça a aletração no nome.')
    else:
         print(f'O  usuario {users} esta disponivel para uso')
