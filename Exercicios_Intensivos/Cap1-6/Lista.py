#Essa varivael vai receber os nomes dos covidados
convidados = []

#Entrada de dados com os nomes dos convidados
convidados.append(input('Seu aniverśario esta chegando, que famoso você quer convidar? '))
convidados.append(input('Qual outro famoso você quer convidar? '))
convidados.append(input('Ok, esse é o ultimo:' ))

print('Tudo bem, vou enviar o convite para eles :)')

#Saida dos convites
print('Olá',convidados[0],'você esta convidado para minha festa!')
print('Olá',convidados[1],'você esta convidado para minha festa!')
print('Olá',convidados[2],'você esta convidado para minha festa!')


#Um convidado não vai poder vir

print("Ou não, acconteceu uma acidente com o",convidados[2],"e ele não vai poder comparecer ")

#Modificar o convidados

convidados[2] = input("Quem você quer que eu convide no lugar dele? ")

#Confirmação do covite
print('O',convidados[0],'confirmou que vai vir!')

print('O',convidados[1],'confirmou que vai vir!!')

print('O',convidados[2],'confirmou que vai vir!')

#Mais convidados

print('Acabamos de encontrar uma mesa maior e podemos chamar mais três convidados')

convidados.insert(0,input('Fale o nome do quarto conviado: '))
convidados.insert(4,input('Fale o nome do quinto covidado: '))
convidados.append(input('Fale o nome do sexto covidado: '))

#Novo Convite

print('Olá',convidados[0],'você esta convidado para minha festa!')
print('Olá',convidados[1],'você esta convidado para minha festa!')
print('Olá',convidados[2],'você esta convidado para minha festa!')
print('Olá',convidados[3],'você esta convidado para minha festa!')
print('Olá',convidados[4],'você esta convidado para minha festa!')
print('Olá',convidados[5],'você esta convidado para minha festa!')

#Reduzir o numer de convidados

print('Parece que não vou conseguir receber a mesa maior a tempo, vamos ter que chamar menos convidados')
print('Infelizmente só vamos poder convidar duas pessoas da lista')


#usar .pop para retirar os convites

Sem_convite = convidados.pop(5)
print('Olá',Sem_convite,"infelizmente tivemos um probrema e tivemos que tirar seu convite")
Sem_convite = convidados.pop(4)
print('Olá',Sem_convite,"infelizmente tivemos um probrema e tivemos que tirar seu convite")
Sem_convite = convidados.pop(3)
print('Olá',Sem_convite,"infelizmente tivemos um probrema e tivemos que tirar seu convite")
Sem_convite = convidados.pop(2)
print('Olá',Sem_convite,"infelizmente tivemos um probrema e tivemos que tirar seu convite")

#Esses continuam convidados

print(convidados[0],'e',convidados[1],", vocês não precisam se preocupar ainda estão convidados")

print('Em seguida a festa foir realizada com sucesso')

del convidados[0]
del convidados[0]
print(convidados)