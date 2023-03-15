# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:34:19 2021

@author: arturo.castro0
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:52:47 2021

@author: acasc
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scl

#como cargar los datos
fichero='ejercicio3c.txt'
datos=np.loadtxt(fichero)

#grado del polinomio a ajustar y numero de puntos dibujados en el ajuste

n=3 
najuste=1000 

f,c=datos.shape
if c==3:
   x,y,sy=np.split(datos,c,axis=1)
   print('\nTipo de ajuste: AJUSTE PONDERADO\n')
else:
   x,y=np.split(datos,c,axis=1)
   sy=np.ones((f,1))
   print('\nTipo de ajuste: AJUSTE SIN PONDERAR\n')

N=len(x) #Número de datos

N=f
a=np.zeros((n+1,N))

for i in range(n+1):
    for j in range(N):
        a[i,j]=x[j,0]**(i)/sy[j,0]
        
b=np.zeros((N,1))

for i in range(N):
    b[i,0]=y[i,0]/sy[i,0]


#Calculo la matriz de curvatura C multiplicando a·aT:
C=np.dot(a,a.T)
Curv=scl.inv(C)
#Calculo el vector de términos independientes B:
B=np.dot(a,b)

#Calculo los parámetros A:
A=np.dot(Curv,B)

#Realizamos ahora la representacion gráfica
xmin=float(min(x))
xmax=float(max(x))

xgraf=np.linspace(xmin,xmax,najuste)

#escribiendo el polinomio acabamos más rapido
ygraf=np.poly1d([A[3],0,0,A[0]])


plt.figure(2)
plt.plot(x,y,'o')
plt.title('Ajuste con el polinomio $y=A_0+A_3x^3$')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.grid(True)
plt.plot(xgraf,ygraf(xgraf)) 

#CÁLCULO DE ERRORES

#Chi cuadrado
Chi2=0
for k in range(N): 
    Chi2=Chi2+(y[k]-ygraf(x[k]))**2/(sy[k]*sy[k])
Chi2=float(Chi2)
#print(Chi2) #hacerlo para todos los valores

#Desviación estándar
sigma2=0
for k in range(N):
    sigma2=sigma2+1.0/(sy[k]*sy[k])
Syx=np.sqrt(N*Chi2/((N-n-1)*sigma2))
Syx=float(Syx)

#Valor medio de las y_k:
ymed=0
for k in range(N):
    ymed=ymed+y[k]/(sy[k]*sy[k])
ymed=ymed/sigma2
ymed=float(ymed)

#Desviación de las y_k respecto a la media:
St=0
for k in range(N):
    St=St+(y[k]-ymed)**2/(sy[k]*sy[k])
St=float(St)

#Coeficiente de determinación:
r2=(St-Chi2)/St

#Coeficiente de correlación:
R=np.sqrt(r2)

#Incertidumbres de los coeficientes:
s=np.copy(A)
m,n=np.shape(A)

#dependiendo de si es ponderado o no calculo la incertidumbre
#de todos los coeficientes Ao,A1,A2,A3

if c==3:
    for i in range(m):
        s[i]=np.sqrt(Curv[i,i])
else:
    for i in range(m):
        s[i,0]=Syx*np.sqrt(Curv[i,i])

print('\nLos resultados del ajuste son:\n')

print('A[%d]=%10.6f    s(A[%d])=%.6f' %(0,A[0],0,s[0]))
print('A[%d]=%10.6f    s(A[%d])=%.6f' %(3,A[3],3,s[3]))

print('\nValor de chi-cuadrado:', Chi2)
print('\nDesviación estándar de la estimación Syx,:', Syx)
print('\nCoeficiente de determinación:', r2)
print('\nCoeficiente de correlación, R:', R)

