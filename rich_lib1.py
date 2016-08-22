from math import *

def factorial(n):
    fac,num = 1,range(2,n+1)
    for n in num:
        fac = fac*n
    return fac

def mi_sine(x,n_max=10):
    x,y = x%(2*pi),0.
    if x <= (pi/2):
        print "intervalo 1"
    elif (pi/2) < x <= pi:
        print "intervalo 2"
        x = pi-x
    elif (pi) < x <= (3*pi/2):
        print "intervalo 3"
        x = (-x-pi)
    else:
        print "intervalo 4"
        x = x-2*pi

    for n in range(n_max):
        p = 2*n+1
        y += ((-1)**n)*(x**(p))/(factorial(p))
    return y