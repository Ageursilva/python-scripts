def count_words(filename):
    """ Conta o numero aproximao de palavras de um arquivo"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #pass = posso utilizar 'pass' para passar a instrução em "branco"
        msg = f'Sorry, the file "{filename}" does not exist'
        print(msg)
    else:
        #Conta o numero aproximado de palavras no arquivo
        words =  contents.split()
        num_words = len(words)
        print(f'The file {filename.title()} has about {str(num_words)} words.')

    filenames = ['alice.txt', 'moby_dick.txt']
    # Diversos aquivos 
    for filename in filenames:
        count_words(filename)

