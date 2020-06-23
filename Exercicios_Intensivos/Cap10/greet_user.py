import json
filename= '/home/ageu/Documentos/git/python-scripts/Exercicios_Intensivos/Cap10/username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print(f'Welcome back {username}')