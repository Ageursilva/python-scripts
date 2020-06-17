prompt = '\nFale alguma coisa, e eu vou repetir para você::'
prompt += '\nDigite "sair" para finalizar o programa. '

mensagem = " "

ativo = True

while ativo:
    mensagem = input(prompt)
    if mensagem.title() ==  'Sair':
        ativo= False
    else:
        print(mensagem.title())