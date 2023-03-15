# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 17:12:45 2021

@author: acasc
"""
import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt

T=4  #periodo de la funcion T=tf-t0 tal que t0=0 y t1=5#período
t0=0 #limite de integración
nk = 8  #numero de términos de k 

def fun(t):
    if t0<=t<T:
        return 1-t/2
    if t>=T:
        return fun(t-T)
    if t<t0:
        return fun(t+T)
    
    
#defino la funcion para los coeficientes llamando a la funcion periodica  
def fak(t,k):
    f=fun(t)
    return f*np.cos(2.*np.pi*t*k/T)

def fbk(t,k):
    f=fun(t)
    return f*np.sin(2.*np.pi*t*k/T)

#Calculo todos los coeficientes
sol=si.quad(fun, t0, t0+T, limit=1000)
a0=sol[0]/T

#para los 8 términos de ak y bk uso un bucle for
ak = np.zeros(nk)
bk=np.zeros(nk)
for i in range(nk):
    def fa(t):
        fa=fak(t,i+1)
        return fa
    sol=si.quad(fa, t0, t0+T, limit=1000)
    ak[i]=2*sol[0]/T

for i in range(nk):
    def fb(t):
        fb=fbk(t,i+1)
        return fb
    sol=si.quad(fb, t0, t0+T, limit=1000)
    bk[i]=2*sol[0]/T

print('\nLOS COEFICIENTES SON:\n')
print('a[0]=%.4f' %a0)
for i in range(nk):
    print('a[%d]=%.4f    b[%d]=%.4f' %(i+1, ak[i], i+1, bk[i] ))



#quiero graficar la gtransformada de fourier
ti=-4
tf=8
t=np.linspace(ti,tf,1000)

fig=plt.figure()
ax=fig.add_subplot(111)

f=np.zeros(len(t))
for i in range(len(t)):
    f[i]=fun(t[i])
    
ax.plot(t,f,'r-',label='función')
ax.set_xlabel('t')
ax.set_ylabel('f(t)')

#defino la funcion de la transformada de fourier y ploteo la aproximacion
suma = 0
for i in range(nk):
    suma = suma + (ak[i]*np.cos(2*np.pi*(i+1)/T*t) + bk[i]*np.sin(2*np.pi*(i+1)/T*t))
def func(t): 
    return a0 + suma
ax.plot(t,func(t),'b-',label='fourier')

plt.xlim([ti,tf])
ax.grid(True)
ax.legend()
plt.savefig('Ej4_Fourier.jpg')
plt.show()




