%pylab inline
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

D=0.1
om=6.2832
om_D=om*np.sqrt(1-D**2)
T=6.0
N=600

y0=4.0
z0=0.0
w0=[y0, z0]

def schwingung(w,t):
    y= w[0]
    z= w[1]
    dy_dt = z
    dz_dt = -2.0*D*om*z-om**2*y
    return [dy_dt, dz_dt]

t = np.linspace(0.0,T,N)
ergebnis = odeint(schwingung, w0, t)

y = ergebnis[:,0]
z = ergebnis[:,1]

plt.subplot(3,1,1)
plt.plot(t,y,"b",linewidth=3)
plt.title("Gedaempfte Schwingung")
plt.grid()
plt.ylabel('Schwingweg y(t)')

plt.subplot(3,1,2)
plt.plot(t,z,"r-",linewidth=3)
plt.xlabel('Zeit (Sekunden)')
plt.grid()
plt.ylabel('Geschwindigkeit y\'(t)')
def exakt(t):
    k1 = y0*np.cos(om_D*t)
    k2 = (z0+y0*D*om)/om_D
    k3 = k2*np.sin(om_D*t)
    y2 = np.exp(-D*om*t)*(k1+k3)
    return y2

y2 = exakt(t)
fehler = y - y2

plt.subplot(3,1,3)
plt.xlabel("t")
plt.ylabel("Fehler")
plt.grid()
plt.plot(t,fehler,"g-",linewidth=3)
plt.show()
