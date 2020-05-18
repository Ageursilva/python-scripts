#usuario=('Ageu',"Luan",'Zé',"Adminu",'Luan','Vitor')

usuario=()


if  not usuario:
        print('A lista esta vazia')

for user in usuario:
    if  user == "Admin":
         print('Olá Adminx, seja bem vindo!')
    else:
        print('Olá',user,"seja vem vindo")

 