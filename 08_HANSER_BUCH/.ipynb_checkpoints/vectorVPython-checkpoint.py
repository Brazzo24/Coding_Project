{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5bc57289",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div id=\"glowscript\" class=\"glowscript\"></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") { window.__context = { glowscript_container: $(\"#glowscript\").removeAttr(\"id\")};}else{ element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import vpython as vp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a58e2a59",
   "metadata": {},
   "outputs": [],
   "source": [
    "def multi_input(text):\n",
    "    s = input(text)\n",
    "    Ist1 = s.split(\",\")\n",
    "    Ist2 = [float(i) for i in Ist1]\n",
    "    return Ist2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cb1227f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Erster Vektor:1,0,0\n",
      "Zweiter Vektor:0,0,2\n"
     ]
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require.undef(\"nbextensions/vpython_libraries/glow.min\");}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require.undef(\"nbextensions/vpython_libraries/glowcomm\");}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require.undef(\"nbextensions/vpython_libraries/jquery-ui.custom.min\");}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require([\"nbextensions/vpython_libraries/glow.min\"], function(){console.log(\"GLOW LOADED\");});}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require([\"nbextensions/vpython_libraries/glowcomm\"], function(){console.log(\"GLOWCOMM LOADED\");});}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require([\"nbextensions/vpython_libraries/jquery-ui.custom.min\"], function(){console.log(\"JQUERY LOADED\");});}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "a = multi_input(\"Erster Vektor:\")\n",
    "b = multi_input(\"Zweiter Vektor:\")\n",
    "u = b[0]-a[0]\n",
    "v = b[1]-a[1]\n",
    "w = b[2]-a[2]\n",
    "vp.scene.autoscale = True\n",
    "vp.scene.background = vp.color.white\n",
    "vp.arrow(axis=vp.vector(a[0],a[1], a[2]), color=vp.color.blue)\n",
    "vp.arrow(axis=vp.vector(b[0],b[1], b[2]), color=vp.color.red)\n",
    "vp.arrow(pos=vp.vector(a[0],a[1],a[2]),axis=vp.vector(u,v,w), color=vp.color.yellow)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce10c051",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c30148c",
   "metadata": {},
   "outputs": [],
   "source": []
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
