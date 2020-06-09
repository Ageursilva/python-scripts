def Nome_Formatado(Primeiro_Nome, Ultimo_Nome):
    Nome_Completo =  Primeiro_Nome+' '+ Ultimo_Nome
    return Nome_Completo.title()

while True:
    print('\nPor favorm, me dia seu nome')
    print("(Digite 'q' para sair )")
    P_Nome= input('Primeiro nome: ')
    if P_Nome == 'q':
         break
    U_Nome = input('Ultimo nome: ')
    if U_Nome == 'q':
         break

    Nome_Completo = Nome_Formatado(P_Nome,U_Nome)
    print(f'\nOlá, {Nome_Completo}!')