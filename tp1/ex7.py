#f(x) = 2x3+x-5

def maFonction(inf,sup,pas):
    for i in range(inf,sup,pas):
        print(2*pow(i,3)+i-5)

maFonction(10,20,2)