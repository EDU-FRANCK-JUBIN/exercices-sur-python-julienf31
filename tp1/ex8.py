X = {'a','b','c','d'}
Y = {'s','b','d'}

print(X)
print(Y)

print('test appartenance c à X : ','c' in X)
print('test appartenance a à Y : ','a' in Y)

print('X-Y : ',X-Y)
print('Y-X : ',Y-X)

print('XuY : ',X.union(Y))
print('X∩Y : ',X.intersection(Y))