
#DERIVADAS PARCIALES========================================EJERCICIO 5
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d

#creo la reticula
L=40
N=10

#creo las matrices auxiliares
T=np.zeros((N,N))
qx=np.zeros((N,N))
qy=np.zeros((N,N))

kb=-0.49
h=4.     #h=int(L/(N-1))

#establezco las condiciones iniciales
T[0,:]=100
T[N-1,:]=0
T[:,0]=75
T[:,N-1]=50

#calculo la solucion de manera iterativa
for k in range(100):
    for i in range(1,N-1):
        for j in range(1,N-1):
            T[i,j]= 0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])
#calculo los flujos de manera iterativa
for i in range(1,N-1):
        for j in range(1,N-1):
            qx[i,j] = -kb*(T[i+1,j]-T[i-1,j])/(2*h)
            qy[i,j]= -kb*(T[i,j+1]-T[i,j-1])/(2*h)
            
#Creo la figura de temperatura
#plt.close("all")
x=np.linspace(0,L,N)
y=np.linspace(0,L,N)
Y,X =np.meshgrid(y,x)

fig=plt.figure()
ax=fig.add_subplot(1,2,1,projection='3d')
ax.plot_wireframe(X,Y,T)
ax.set_xlabel('x [cm]')
ax.set_ylabel('y [cm]')
ax.set_zlabel('T [K]')
ax.set_title('Temperatura')

#Flechitas con flujos para qx y qy:
X=np.arange(0,N)
Y=np.arange(0,N)
X,Y=np.meshgrid(X,Y)
fig1=plt.figure()
ax1=fig1.add_subplot(1,2,2)
ax1.quiver(X,Y,qy,qx,pivot='middle')
ax1.set_title('Flujo de calor',size=20)
ax1.plot(X,Y,'ro')
ax1.set_title(u'100ºC',fontsize=11)
ax1.set_ylabel(u'75ºC')
ax1.set_xlabel(u'0ºC')
ax2=ax1.twinx()
ax2.set_ylabel(u'50ºC')
plt.savefig('Ej5_PDEs.jpg')