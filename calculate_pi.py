import math

pi = 1.0

for i in range(1,100000):
    t = (4.0*i*i)/(4.0*i*i-1.0)
    pi = pi * t

print('real pi')
print(math.pi)

print('my pi')
print(2*pi)

print('difference')
print(math.pi-2*pi)
