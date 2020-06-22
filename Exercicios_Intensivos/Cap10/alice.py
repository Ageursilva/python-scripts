filename =  '/home/ageu/Documentos/git/python-scripts/Exercicios_Intensivos/Cap10/alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f'Sorry, the file "{filename}" does not exist'
    print(msg)
else:
    #Conta o numero aproximado de palavras no arquivo
    words =  contents.split()
    num_words = len(words)
    print(f'The file {filename.title()} has about {str(num_words)} words.')