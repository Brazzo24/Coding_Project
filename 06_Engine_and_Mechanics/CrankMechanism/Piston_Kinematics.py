#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import necessary packages
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# In[2]:


#input parameters
r = 1.0 #crank radius
l = 4.0 #connecting rod lenght
rot_num = 4 #number of crank rotations
increment = 0.1 #angle increment


# In[3]:


#create the angle array, where the last angle is the number of rotations*2*pi
angles = np.arange(0, rot_num*2*pi+increment, increment)


# In[4]:


angles


# In[5]:


X1 = np.zeros(len(angles)) #array of crank x-positions: Point 1


# In[6]:


X1


# In[7]:


Y1 = np.zeros(len(angles)) #array of crank y-positions: Point 1


# In[8]:


X2 = np.zeros(len(angles)) #array of rod x-positions: Point 2


# In[9]:


Y2 = np.zeros(len(angles)) #array of rod y-positions: Point 2


# In[10]:


#find the crank and connecting rod positions for each angle
for index, theta in enumerate(angles, start=0):
    x1 = r*cos(theta) # x-coordinate of the crank: Point 1
    y1 = r*sin(theta) # y-coordinate of the crank: Point 1
    x2 = 0 # x-coordinate of the rod: Point 2
    y2 = r*sin(theta) + sqrt(1**2 - (r*cos(theta))**2)
    
    X1[index] = x1 #crankshaft x-position
    Y1[index] = y1 #crankshaft y-position
    X2[index] = x2 #connecting rod x-position
    Y2[index] = y2 #connecting rod x-position


# In[17]:


#set up the figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
ax.set_title('Piston Motion Animation')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')


# In[12]:


#initialize functino
def init():
    line.set_data([], [])
    return line,


# In[13]:


#animation function
def animate(i):
    x_points = [0, X1[i], X2[i]]
    y_points = [0, Y1[i], Y2[i]]
    
    line.set_data(x_points, y_points)
    return line,


# In[15]:


#call the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(X1), interval=40, blit=True, repeat=False)
## to save the animation, uncomment the line below
##ani.save('offset_piston_motion_animation.mp4',fps=30, extra_args=['vcodec', 'libx264'])

#show the animation
plt.show()


# In[ ]:




