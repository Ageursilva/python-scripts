#Entrada de dados
Email = int(input('Quantos e-mails você tem na caixa de entrada? '))

while Email < 100 :
    print('Você tem poucos e-mails :)')
    Novos = int(input('Quantos novos e-mails você recebeu?'))
    Email = Email + Novos
else:
    print('Sua caixa de e-mails esta lotada :O !!!')
