"""
==========================
integral animation
==========================

"""
from matplotlib import animation as animation
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np


# design figure
fig = plt.figure()
ax = fig.add_subplot(111,ylim=[0,10],xlim=[0,10])

# custormer function here
dx = 0.1
x = np.arange(0,10,dx)
y1 = np.log(x+1)*np.sin(x)+5

line, = plt.plot([],[])

def animate(i):
    thisx = x[20:20+i]
    thisy = y1[20:20+i]
    line.set_data([],[])

    # fill_between() function will cover previous frame, fill white before fill color
    plt.fill_between(thisx,0,thisy,color='w')
    plt.fill_between(thisx,0,thisy,color='b',alpha=0.3)

    return line


def init():
    # clear figure everytime, or fill result will leave to new animation
    fig.clf()
    ax = fig.add_subplot(111,ylim=[0,10])
    line, = plt.plot(x,y1,color='b')

    return line

ani=animation.FuncAnimation(fig,animate,np.arange(1,60),interval=100,init_func=init,blit=False)

plt.show()
