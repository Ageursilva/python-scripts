import os 
file = ' /home/ageu/Documentos/git/python-scripts/Exercicios Intensivos/Cap10/py/pi_digits.txt'
with open('file') as file_object:
    contents =  file_object.read()
    print(contents)