#Informações das pizzas

pizza = {
    'massa' : 'grossa',
    'recheio' : ['cogumelo', 'queijo extra']
    
}

print(f'Você pediu uma {pizza["massa"]}, agora escolha o recheio.')

print('\nEsses são os saborres disponivel:')
for sabores in pizza['recheio']:
    print('\n\t', sabores)