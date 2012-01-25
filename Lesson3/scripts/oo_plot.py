import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.*np.pi, 2.*np.pi, 100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
line = ax.plot(x, y)
ax.set_xlim([-2*np.pi,2*np.pi])

plt.show()
