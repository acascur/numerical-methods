# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:16:38 2021

@author: acasc
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:48:33 2021

@author: acasc
"""
#==================================================EJERCICIO 2

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d
 
#creo la reticula
N = 40
V = np.zeros((N,N))
#establezco las condiciones iniciales
V [0,:] = 100
V [N-1,: ] = -100
#calculo el potencial de manera iterativa
for k in range(100):
    for i in range(1,N-1):
        for j in range(1,N-1):
            V[i,j]= 0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1])
            
#hago la gráfica
x = np.arange(0,N)
y = np.arange(0,N)
y,x = np.meshgrid(y,x)
fig= plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax = p3d.Axes3D(fig)
ax.plot_wireframe(x,y,V)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()