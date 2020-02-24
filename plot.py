import matplotlib
#matplotlib.use('AGG')
import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(0,10,1000)
y=np.cos(2*np.pi*x)*np.exp(-x)+1
plt.plot(x,y,linewidth=1)

plt.show()

