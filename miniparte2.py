#Universidad del Valle de Guatemala
#Javier Capio - 17077
#Guillermo Sandoval - 17577

#Ejercicio4 integral e^-x^2

import random
import math
import matplotlib.pyplot as plt
import numpy as np

#Numero de iteraciones
it = 100000
y = []

#Puntos random generados
y = np.random.rand(it)
value = np.array([])
for i in y:
    value = np.append(value, [math.e**(-((1/i-1)**2))/(i**2)])


dentroFuncion = sum(value)
proporcion = 2*(dentroFuncion/it)

print('La aproximacion es: ' + str(proporcion))
