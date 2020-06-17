file = '/home/ageu/Documentos/git/python-scripts/Exercicios_Intensivos/Cap10/py/pi_million_digits.txt'
with open(file) as file_object:
    lines = file_object.readlines()

pi_string= ' '
for line in lines:
    pi_string += line.strip()

print(pi_string[:52]+'...')
print(len(pi_string))

birthday = input('Enter your birthday, in the forme mmddyy: ')
if birthday in pi_string:
    print("Your birthday appers in the fisrt million digits of pi! ")
else:
     print("Your birthday does not appers in the fisrt million digits of pi! ")
