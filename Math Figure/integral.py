"""
==========================
integral plot
==========================

"""
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,ylim=[0,10],xlim=[0,10])


dx = 0.1
x = np.arange(0,10,dx)

# customer function
y1 = np.log(x+1)*np.sin(x)+5
f = lambda x:np.log(x+1)*np.sin(x)+5
line, = plt.plot(x,y1,color='b')

# range of fill,x and y are the same size
fillx = x[20:81]
filly = y1[20:81]
plt.fill_between(fillx,0,filly,color='b',alpha=0.3)

# add scatter
plt.scatter([x[20],x[20]],[0,f(x[20])], 50, color ='b')
plt.plot([x[20],x[20]],[0,f(x[20])], color ='b', linewidth=1.5, linestyle="--")

plt.scatter([x[80],x[80]],[0,f(x[80])], 50, color ='b')
plt.plot([x[80],x[80]],[0,f(x[80])], color ='b', linewidth=1.5, linestyle="--")

# add annotate
ax.annotate(r'$x=a$', xy=(x[20], f(x[20])), xytext=(x[20], f(x[20])+0.5))
ax.annotate(r'$x=b$', xy=(x[80], f(x[80])), xytext=(x[80], f(x[80])+0.5))
ax.annotate(r'$Area=\int_{a}^{b}f(x)\mathrm{d}x$', xy=(x[40], 1), xytext=(x[40], 1))

# save fig
#fig.savefig('integral.png',dpi=200)
plt.show()
