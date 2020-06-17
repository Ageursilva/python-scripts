import math
# Entrada dos dados

CordX = float(input('Digite a coordenada X:'))
CordY = float(input('Digite a coordendada Y:'))
CordX2 = float(input('Digite a coordenada X2:'))
CordY2 = float(input('Digite a coordenada Y2:'))

#Faz o calculo

distancia = math.sqrt((CordX-CordX2)**2 + (CordY-CordY2)**2)

#Saida de dados

if distancia > 10:
    print('Longe')
else :
    print('Perto')
