#Esse programa vai receber alguns intens para compras e depois mostar

#A varivavel "itens" vai receber os dados

itens = []


print('Oi, eu vi que você vai fazer umas compras, posso te ajudar?')
print('Eu posso armazenar até 9 itens para sua lista, vamos lá? ')


#Entrada de dados que vão ser armazenados na varivael "itens"

itens.append((input("Digite o primeiro item: ")))

itens.append((input("Digiteo segundo: ")))

itens.append((input("Terceiro item: ")))

itens.append((input("Quarto item: ")))

itens.append((input("Quinto item: ")))

itens.append((input("Sexto item: ")))

itens.append((input("Sétimo item: ")))

itens.append((input("Oitavo item: ")))

itens.append((input("Ultimo item: ")))

print('Ok, todos os itens foram armazenados')

#Saida de dados

print('Os três primeiros intens são:',itens)
#print('Os intens do meio são:',itens(4:7))

#print('Os ultimos intens são:'itens(7:)))