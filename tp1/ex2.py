import math

number = input('Entrez un entier strictement positif : ')

diviseur = []

for i in range(2,int(number)):
    if int(number)%i == 0 :
        diviseur.append(i)

if len(diviseur) == 0:
    print('Aucun diviseurs propres, il est premier')
else:
    print('Diviseur propres sans répétitions :',diviseur,'(soit ',len(diviseur),'diviseurs propres)',sep=' ',end='.')