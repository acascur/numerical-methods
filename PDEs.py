# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:59:15 2021

@author: acasc
"""
"""
#RECORDATORIO

x=np.arange(10)
print(x,'\n')

print(x[1],'es x[1]') #segubndo elemento de la lista

print(x[1:4]) #del segundo al tercero??

print(x[-2]) #segundo elemento desde atras

print(x[-4:]) #cuenta los ultimos 4 elementos de la lista

D=3

Y=np.zeros([D,D]); #creo matriz cuadrada de 3x3

print(Y[D-1:]) #primera fila de la matrix
print(Y[0,:])

"""

#==================================================EJERCICIO 1
#%%

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d
import seaborn as sns 

#Creamos la reticula cuadrada de nuestro problema y sus condiciones iniciales

N = 40 #dimension cuadricula
V = np.zeros((N,N)) #creo cuadricula de 40x40
V [0,:] = 100 #fijo el potencial a 100 en la primera fila

#caslculamos el potencial

for k in range(100): #numero de iteraciones
    for i in range(1,N-1): #i desde 1 hasta 38 inclusive
        for j in range(1,N-1): #j desde i hasta 38 inclusive
            V[i,j]= 0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1])
            

x = np.arange(0,N)
y = np.arange(0,N)
y,x = np.meshgrid(y,x)
fig= plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax = p3d.Axes3D(fig)
ax.plot_wireframe(x,y,V) #ax.plot_surface(X, Y, V)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

sns.heatmap(V)

#==================================================EJERCICIO 2
#%%

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d

N = 40
V = np.zeros((N,N))
V [0,:] = 100
V [N-1,: ] = -100
for k in range(100):
    for i in range(1,N-1):
        for j in range(1,N-1):
            V[i,j]= 0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1])
            

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

sns.heatmap(V,cmap='icefire')

#DERIVADAS PARCIALES========================================EJERCICIO 3
#%%

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d
import seaborn as sns 

N = 100
V = np.zeros((N,N))

for k in range(100): #numero de iteraciones
    for i in range(1,N-1):
        for j in range(1,N-1):
            if 59<i<79 and 19 < j <39:
                rho = -1.0
            else: 
                rho = 0.
                
            V[i,j]=0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1]+ rho/(8.85e-12))

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

sns.heatmap(V,cmap='icefire')

#DERIVADAS PARCIALES========================================EJERCICIO 4
#%%

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d
import seaborn as sns 

N = 100
V = np.zeros((N,N))

for k in range(100): #numero de iteraciones
    for i in range(1,N-1):
        for j in range(1,N-1):
            if 59<i<79 and 19 < j <39:
                rho= -1.0
            elif 19<i<39 and 59<j<79:
                rho = 1.0
            else: 
                rho = 0.               
            V[i,j]=0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1]+ rho/(8.85e-12))

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

sns.heatmap(V)

#DERIVADAS PARCIALES========================================EJERCICIO 5
#%%

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d
import seaborn as sns 

L=40
N=10

T=np.zeros((N,N))
qx=np.zeros((N,N))
qy=np.zeros((N,N))

kb=-0.49
h=4.     #h=int(L/(N-1))

T[0,:]=100
T[N-1,:]=0
T[:,0]=75
T[:,N-1]=50

for k in range(100):
    for i in range(1,N-1):
        for j in range(1,N-1):
            T[i,j]= 0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])

for i in range(1,N-1):
        for j in range(1,N-1):
            qx[i,j] = -kb*(T[i+1,j]-T[i-1,j])/(2*h)
            qy[i,j]= -kb*(T[i,j+1]-T[i,j-1])/(2*h)
            
#Creo la figura de temperatura
#plt.close("all")
x=np.linspace(0,L,N)
y=np.linspace(0,L,N)
Y,X =np.meshgrid(y,x)

fig=plt.figure(figsize=(8,8))
ax=p3d.Axes3D(fig)
ax.plot_wireframe(X,Y,T)
ax.set_xlabel('x [cm]')
ax.set_ylabel('y [cm]')
ax.set_zlabel('T [K]')
ax.set_title('Temperatura')

#sns.heatmap(T)


#Flechitas con flujos para qx y qy:
X=np.arange(0,N)
Y=np.arange(0,N)
X,Y=np.meshgrid(X,Y)
fig1=plt.figure(figsize=(8,8))
ax1=fig1.add_subplot(1,1,1)
ax1.quiver(X,Y,qy,qx,pivot='middle')
ax1.plot(X,Y,'ro')

#DERIVADAS PARCIALES========================================EJERCICIO 6
#%%

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d
import seaborn as sns 

Nt=50    #T=1 hora y At=0.02h
Nx=10    #L=0,5m y Ax=5cm
r=0.049*0.02/(0.05**2) #calculo de r con los datos del problema

T=np.zeros((Nx,Nt))

for i in range(Nx):   #tenemos que T(x,0)=100ºC como condicion inicial y T(0,t)=T(x,t)=0
    T[i,0]=100        #T[:0]=100 probar con esto no funciona
 
for k in range(100):
    for i in range(1,Nx-1):
        for j in range(0,Nt-1):
            T[i,j+1]=T[i,j]+r*(T[i+1,j]+T[i-1,j]-2*T[i,j])


x = np.arange(0,Nx)
y = np.arange(0,Nt)
X,Y =np.meshgrid(y,x)
fig=plt.figure(figsize=(8,8))
ax=p3d.Axes3D(fig)
ax.plot_wireframe(X,Y,T)


plt.show()

sns.heatmap(T,cmap='rocket')

#===========================
#%%
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d

Nt = 50
Nx = 10
T = np.zeros((Nt,Nx))
r = 0.049*0.02/(0.05**2)
T[0,1:Nx-1]=100

for k in range(100):
    for j in range(0,Nt-1):
        for i in range(1,Nx-1):
            T[j+1,i]= T[j,i]+r*(T[j,i+1]+T[j,i-1]-2*T[j,i]) 
            
x = np.arange(0,Nx)
y = np.arange(0,Nt)
y,x = np.meshgrid(x,y)
fig= plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection= '3d')
ax.plot_wireframe(x,y,T)
"""
