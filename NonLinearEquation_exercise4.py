# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:05:35 2021

@author: acasc
"""
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt


#dominio de representacion
xini=-4 #Valor inicial del dominio en x
xfin=4 #Valor final del dominio en x

#Dibujo la gráfica:
x=np.linspace(xini,xfin,100)
y1=x**2-1.2*x**3
y2=1-3*x

fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111)
ax.plot(x,y1,'r-')
ax.plot(x,y2,'b-')
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_xlim(min(x),max(x))
ax.set_ylim(-20,20)
ax.grid(True)

#Creo una función con las funciones residuales y busco puntos (x1,x2) que anulen (f1,f2)
def ffnolineal(x):
    x1,x2=x
    f1=1.2*x1**3-x1**2+x2
    f2=3*x1+x2-1
    return [f1,f2]

#Divido el dominio de las funciones en intervalos:
xaux=np.copy(x)
yaux=1-3**xaux
xsol=[]
ysol=[]

#Llamo a la función fsolve en cada uno de esos intervalos:
for i in range(len(xaux)):
    guess=[xaux[i],yaux[i]]
    sol=sco.fsolve(ffnolineal,guess)
    #Aproximo la solución según unos decimales deseados en mi caso 4:
    x=np.round(sol[0],decimals=4)
    y=np.round(sol[1],decimals=4)
    #Veo si la nueva solución no está ya en el vector de soluciones y sino la añado al array:
    if x not in xsol:
        xsol.append(x)
        ysol.append(y)
    else:
        pass

#grafico las soluciones
for i in range(len(xsol)):
    ax.scatter(xsol[i],ysol[i],color='green',marker='o')

print('\nEl número de soluciones es: %d \n' %(len(xsol)))
for i in range(len(xsol)):
    print('x[%d]= %8.4f    y[%d]= %8.4f' %(i+1,xsol[i],i+1,ysol[i]))
    


    