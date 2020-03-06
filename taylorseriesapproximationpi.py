import math
import numpy as np
import matplotlib.pyplot as plt
import math
#taylor series of arcsinnx
x = .5
arcsine = x**1/math.factorial(1) + x**3/math.factorial(3) + 9*x**5/math.factorial(5) + 225*x**7/math.factorial(7) + 35*x**9/1152
print(arcsine)
print (6*arcsine)


#for loop for taylor series
x = .5
arcsine2 = 0
for n in range(50):
    arcsine2+= ((math.factorial(2*n))/((2**(2*n))*((math.factorial(n))**2)*(2*n + 1)))*(x**(2*n + 1))

print (6*arcsine2)


def func_sin(x, n):
    generalarcsine = 0
    for i in range(n):
        generalarcsine+= ((math.factorial(2*n))/((2**(2*n))*((math.factorial(n))**2)*(2*n + 1)))*(x**(2*n + 1))
