hora1= int(input("Digite apenas a hora da primeira entrada:"))
min1= int(input("Digite apenas os minutos da primeira entrada:"))
hora2= int(input("Digite apenas a hora da segunda entrada:"))
min2= int(input("Digite apenas os minutos da segunda entrada:"))

soma_hora= hora1 + hora2
soma_minutos= min1 + min2

if soma_minutos >=60:
    soma_hora = soma_hora + 1
    soma_minutos = soma_minutos-60

if soma_hora >=24:
    soma_hora = soma_hora-24
if soma_hora >= 24:
    soma_hora = soma_hora - 24

if soma_hora >=12:
    soma_hora = soma_hora-12
print(soma_hora, soma_minutos)
