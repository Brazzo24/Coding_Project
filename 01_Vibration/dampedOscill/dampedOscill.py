import numpy as np
import matplotlib.pyplot as plt
from math import sin, sqrt
from scipy.integrate import odeint

#constants and stuff
k = 2.0
m = 0.5
g = 0.05 #light damping
F = 1.0
w0 = sqrt(k/m)

w = 0.99 * w0
tmax = 150
dt = 0.01
t = 0
x = 0
v = 0
a = 0

#equation of motion
#m d2x/dt2 - 2 g dx/dt + kx = F sin wt

print('w0 = %f\n'%w0)

def force(x, v, t):
    return -g*v - k*x + F*sin(w*t)

X = [0.]
T = [0.]
FF = [1.]

while t<tmax:
    f = force(x, v, t)
    a = f/m
    x = x + v * dt + 0.5 * a *dt *dt
    v = v + a *dt
    FF.append(F*sin(w*t))
    t = t + dt
    X.append(x)
    T.append(t)

plt.figure()
plt.plot(T, X)
plt.plot(T, FF)
plt.title('amplitude response of lightly damped driven oscillator')
plt.legend(('displacement', 'force'))
plt.xlabel('time')
plt.show()
