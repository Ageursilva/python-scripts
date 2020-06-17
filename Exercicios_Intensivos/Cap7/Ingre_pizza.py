prompt = "\nPor favor, digite o ingredite que vocêr quer na pizza"
prompt  += "\nQuando terminar, digite 'sair "

ingredientes = " "

sabor= True

while sabor:
    ingredientes = input(prompt)

   
    if ingredientes.title() == 'Sair':
        sabor= False
    else:
        print(ingredientes)                  