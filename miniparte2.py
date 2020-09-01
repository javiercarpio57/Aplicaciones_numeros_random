#Universidad del Valle de Guatemala
#Javier Capio - 17077
#Guillermo Sandoval - 17577

#Ejercicio1 El triangulo de Shierpinski

import random
import math
import matplotlib.pyplot as plt

#Puntos donde empieza el fractal
p1, p2, p3 = 0.20, 0.30, 0.50
#Numero de iteraciones
it = 100000
x, y = [],[]

def transf(x, y, prob):
    
    if(prob <= p1):
        x = x/2
        y = y/2
    elif(prob <= (p1+p2) and prob > p1):
        x = x/2 + 0.5
        y = y/2
    elif(prob <= (p1+p2+p3) and prob > (p1+p2)):
        x = x/2 + 0.25
        y = y/2 + 0.5
    return x, y

pointx = random.random()
pointy = random.random()

for iteracion in range(0, it):
    prob = random.random()
    px, py = transf(pointx, pointy, prob)
    x.append(px)
    y.append(py)
    pointx = px
    pointy = py

plt.scatter(x, y, s = 0.3, edgecolor = 'yellow')
plt.show()