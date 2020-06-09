respostas = {}

# Flag para dizer que a enquente  esta ativa

questionatio_ativo =  True
while questionatio_ativo:

    #pedido de nome e respostas

    nome =  input('\nQual seu nome?  ')

    resposta = input(' Que cidade você gostaria de visistar? ')

    #Arma as repostas no dicionario
    
    respostas[nome] =  resposta

    #Verifcar se outros usuario vai responder

    Repetir = input('Outro usuario gostaria de responder? (S / N ) ')
    
    if Repetir.title() == "N":

        questionatio_ativo = False

# Fim da enquete 
           
print('\n---- Resultado dda pesquisa ----')

for nome, resposta in respostas.items():

    print(f'{nome.title()} gostatia de visitar {resposta.title()} ')
