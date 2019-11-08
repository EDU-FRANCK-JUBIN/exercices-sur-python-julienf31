number = input('Saisissez un chiffre entre 1 et 3999 : ')

if int(number) < 1 or int(number) > 3999:
    print('Mauvais range')
    exit()

#I = 1 en chiffre romain,
#V = 5 en chiffre romain,
#X = 10 en chiffre romain,
#L = 50 en chiffre romain,
#C = 100 en chiffre romain,
#D = 500 en chiffre romain,
#M = 1000 en chiffre romain,

str_num = str(number)

unit = [" ","I","II","III","IV","V","VI","VII","VIII","IX"]
diz = [" ","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
cent = [" ","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
mil = [" ","M","MM","MMM"]

res = ""

if len(str_num) == 4:
    res = mil[int(str_num[0])]+cent[int(str_num[1])]+diz[int(str_num[2])]+unit[int(str_num[3])]
elif len(str_num) == 3:
    res = cent[int(str_num[0])]+diz[int(str_num[1])]+unit[int(str_num[2])]
elif len(str_num) == 2:
    res = diz[int(str_num[0])]+unit[int(str_num[1])]
elif len(str_num) == 1:
    res = unit[int(str_num[0])]

print(res)