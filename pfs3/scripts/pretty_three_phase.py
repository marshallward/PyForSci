import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.*np.pi, 2.*np.pi, 50)
phase = np.arange(0., 2*np.pi, 2*np.pi/3.)

y_p = [np.sin(x + p) for p in phase]
style = ['r:', 'g--', 'py']

pdata = zip(y_p, style)
for y,s in pdata:
    plt.plot(x, y, s)
plt.show()
