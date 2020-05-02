Segundos_Str = input('Por vavor, entre com o número de segundos:')
Total_Segs = int(Segundos_Str)


Dias = Total_Segs // 86400
Seg_Restantes1 = Total_Segs % 86400
Horas = Seg_Restantes1 // 3600
Segundos_Restantes = Total_Segs % 3600 
Minutos =  Segundos_Restantes // 60 
Segundos_Restantes_Final = Segundos_Restantes % 60


print(Dias,'dias',Horas,'horas,',Minutos,'minutos e', Segundos_Restantes_Final,'segundos.')


