import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
HTML(ani.to_html5_video())

# Turn off matplotlib plot in Notebook
plt.ioff()
# Pass the ffmpeg path
plt.rcParams['animation.ffmpeg_path'] = '/Users/chen5/Downloads/ffmpeg'

fig, ax = plt.subplots()

line, = ax.plot([])

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.1, 1.1)


def animate(frame_num):
    y = np.sin(x + 2*np.pi * frame_num/100)
    line.set_data((x, y))
    return line

anim = FuncAnimation(fig, animate, frames=100, interval=20)

video = anim.to_html5_video()
html = display.HTML(video)
display.display(html)
plt.close()