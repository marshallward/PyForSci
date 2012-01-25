import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.*np.pi, 2.*np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(x + 2.*np.pi/3.)

plt.fill_between(x, y1, y2)
plt.show()
