prompt = '\nFale alguma coisa, e eu vou repetir para você::'
prompt += '\nDigite "sair" para finalizar o programa. '

mensagem = " "

while mensagem.title() != 'Sair':
    mensagem = input(prompt)
    print(mensagem.title())

    if mensagem.title() != 'Sair':
        print(mensagem)