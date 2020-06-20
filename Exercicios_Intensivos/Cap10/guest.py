filename = "/home/ageu/Documentos/git/python-scripts/Exercicios_Intensivos/Cap10/guest.txt"
#Local onde esta  o arquivo para recber os itens

with open(filename,'a') as file_object:
# 'a' diz para abrir o arquivo para concatenar
    while True:
        name = input('Digite o nome do convidado: ')
        print('Digite "Q" para sair')

        if name.title() == 'Q':
            break
        print (f'Olá {name.title()}, seja bem vindo!')
        file_object.write(f'\n{name}')
        #Escreve os nomes no aquirvo guest.txt

with open(filename) as file_object:
    file = file_object.read()
    print('Lista de todos os convidados')
    print(file)