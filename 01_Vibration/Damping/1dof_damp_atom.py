import numpy as np
from numpy.linalg import inv
import sympy as smp
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from sympy import *

#variables
I = 2.0
k = 2.0
c = 0.0 #critical damping = 2*sqrt(I*k)

T0 = 1.0
delta_t = 0.1
omega = 1.0
time = np.arange(0.0, 20.0, delta_t)

#initial state
y = np.array([0,1]) #[velocity, displ.]

A = np.array([[I, 0],[0, 1]])
B = np.array([[c,k],[-1,0]])
T = np.array([0.0,0.0])

Y = []
Y_d = []
torque = []

#time-stepping solution#
for t in time:
    if t <= 15:
        T[0] = T0 * np.cos(omega*t)
    else:
        T[0] = 0.0

    y = y + delta_t * inv(A).dot(T - B.dot(y) )
    Y.append(y[1])
    Y.append(y[0])
    torque.append(T[0])

    KE = 0.5 * I * y[0]**2
    PE = 0.5 * k * y[1]**2

    if t % 1 <= 0.01:
        print('Total Energy: ', KE+PE)

#plot the result
t = [i for i in time]

plt.plot(t,Y)
plt.plot(t,Y_d)
plt.plot(t,torque)
plt.grid(True)
plt.legend(['Displacement', 'Torque'], loc='lower right')


plt.show()

print('Critical Damping: ', np.sqrt((-c**2 + 4*I*k) / 2.0*I))
print('Natural Frequency: ', np.sqrt(k/I))
