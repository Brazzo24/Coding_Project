{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "818a8fc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import vpython\n",
    "from vpython import*\n",
    "import numpy as np\n",
    "\n",
    "x1, y1, z1, x2, y2, z2 = np.load('../3d_Pendulum/Data')\n",
    "ball1 = vpython.sphere(color.green, radius = 0.3, make_trail=True, retain=20)\n",
    "ball2 = vpython.sphere(color.blue, radius = 0.3, make_trail=True, retain=20)\n",
    "rod1 = cylinder(pos=vector(0,0,0), axis=vector(0,0,0), radius=0.05)\n",
    "rod2 = cylinder(pos=vector(0,0,0), axis=vector(0,0,0), radius=0.05)\n",
    "#base cylinder(pos=vector(0,-4,0), axis=vector(0,-0.1,0), radius = 6)\n",
    "base = box(pos=vector(0,-4.25,0), axis=vector(0,0.1,0).\n",
    "          size=vector(10,0.5,10))\n",
    "s1 = cylinder(pos=vector(0,-3.99,0), axis=vector(0,-0.1,0), radius=0.8, color=color.gray(luminance=0.7))\n",
    "s2 = cylinder(pos=vector(0,-3.99,0), axis=vector(0,-0.1,0), radius=0.8, color=color.gray(luminance=0.7))\n",
    "\n",
    "print('Start')\n",
    "i=0\n",
    "while True:\n",
    "    i = i + 1\n",
    "    i = %len(x1)\n",
    "    ball1.pos = vector(x1[i], z1[i], y1[i])\n",
    "    ball2.pos = vector(x2[i], z2[i], y2[i])\n",
    "    rod1.axis = vector(x1[i], z1[i], y1[i])\n",
    "    rod2.pos = vector(x1[i], z1[i], y1[i])\n",
    "    rod2.axis = vector(x2[i]-x1[i], z2[i]-z1[i], y2[i]-y1[i])\n",
    "    s1.pos = vector(x1[i], -3.99, y1[i])\n",
    "    s2.pos = vector(x2[i], -3.99, y2[i])\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
