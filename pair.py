tt = [32,5,12,8,3,75,2,15]
odd = []
pair = []

for num in tt:
    if num % 2 == 0:
        pair.append(num)
    else:
        odd.append(num)

print('Pair : ', pair)
print('Odd : ', odd)