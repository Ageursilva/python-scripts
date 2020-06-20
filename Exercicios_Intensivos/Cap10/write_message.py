filename = '/home/ageu/Documentos/git/python-scripts/Exercicios_Intensivos/Cap10/programing.txt'

with open(filename, 'w') as file_object: 
    file_object.write(input('Digite alguma coisa: '))