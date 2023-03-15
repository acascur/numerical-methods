# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:53:14 2021

@author: acasc
"""

#Hayar el mínimo de una funcion de dos variables

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

#definimos la función
def fund_2(v):
    x,y=v
    z=x*np.exp(-1*(x**2+y**2))
    return z

#añadimos limites
xi , xf = -1,1
yi , yf = -1,1

#estimacion inicial
p0=(0.,0.)

#intervalo de busqueda
bnds=((xi , xf),(yi , yf))


#puntos en los que la funcion sera evaluada
npuntos=75
x=np.linspace(xi,xf,npuntos) #vector cord en x
y=np.linspace(yi,yf,npuntos) #vector cord en y

#Hago la gráfica
X , Y = np.meshgrid(x,y)
Z =fund_2([X,Y])
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111,projection='3d')
ax.plot_wireframe(Y, X, Z, color='b', rstride=3, cstride=250)
ax.set_title('$f(x,y)=x·exp(x^2+y^2)$')
ax.set_xlabel('X')
ax.set_ylabel('Y')

#para calcular los mínimos
sol=sco.minimize(fund_2, p0, bounds=bnds)
xmin=sol.x[0]
ymin=sol.x[1]
fmin=fund_2(sol.x)
#Grafico el mínimo global
ax.scatter(xmin,ymin,fmin,color='red')

print('El mínimo de la función se encuentra en xmin=%5.3f  ymin=%5.3f   fmin=%5.3f' % (xmin,ymin,fmin) )

