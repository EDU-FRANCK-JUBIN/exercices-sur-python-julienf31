import math

def fact(a):
    res = 1
    for i in range(1,a+1):
        res *= i
    return res

number = input('Entrez n : ')

if int(number) < 50:
    print('Saisissez un n > 50')
    exit()

result = 0;

for i in range(0,int(number)):
    #somme 1/n!
    result += 1/fact(i)

result_tab = [
    ['resultat',result],
    ['erreur',abs(result-math.e)/result]
]

print(result_tab)


