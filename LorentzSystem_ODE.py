# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:00:43 2021

@author: acasc
"""
import scipy.integrate as si
import numpy as np
import matplotlib.pyplot as plt

sigma=10.
b=8./3
r=28.

def deriv7(f,t):
    x,y,z=f
    dx_dt=sigma*(y-x)
    dy_dt=r*x-y-x*z
    dz_dt=x*y-b*z
    return dx_dt,dy_dt,dz_dt

x0=5.;y0=5.;z0=5.
ti=0.;tf=12.
t=np.linspace(ti,tf,10000)

est_ini=[x0,y0,z0]

sol7=si.odeint(deriv7,est_ini,t)

x=[];y=[];z=[]

filas,columnas=np.shape(sol7)

for i in range (filas):
    x.append(sol7[i,0])
    y.append(sol7[i,1])
    z.append(sol7[i,2])
    

plt.subplot(2,3,1)
plt.plot(x,y,'b')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)
plt.title('y(t) frente a x(t)')

plt.subplot(2,3,2)
plt.plot(x,z,'r')
plt.xlabel('x')
plt.ylabel('z(x)')
plt.grid(True)
plt.title('z(t) frente a x(t)')

plt.subplot(2,3,3)
plt.plot(y,z,'g')
plt.xlabel('y')
plt.ylabel('z(y)')
plt.grid(True)
plt.title('z(t) frente a y(t)')

plt.tight_layout()
plt.savefig('Ej7_ODEs_fig1.jpg')
plt.show()

plt.subplot(1,1,1,projection='3d')
plt.plot(x,y,z,'b-')
plt.title('z=z(x,y)')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('Ej7_ODEs_fig2.jpg')
plt.show()