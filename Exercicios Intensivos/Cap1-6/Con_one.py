#Teste condicional para saber quem é mais velhro


#Essa variavel recebe a minha idade

MinhaIdade=[]

MinhaIdade.append(input('Qual sua idade? '))


#Essa recebe a idade de outra pessoa para o teste

OutraIdade =[]

OutraIdade.append(input("Qual a idade do seu amigo?"))

if MinhaIdade <OutraIdade:
    
    print('Você é mais novo que seu amigo')
elif MinhaIdade == OutraIdade:
     print('Vocês tem a mesma idade')
elif  MinhaIdade>OutraIdade:
    print('Você é mais velho')   