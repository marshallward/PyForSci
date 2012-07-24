import numpy as np
import matplotlib.pyplot as plt

x_ax = np.linspace(-2., 2., 100)
y_ax = np.linspace(-2., 2., 100)

x, y = np.meshgrid(x_ax, y_ax)
z = (x - 0.5)*np.exp(-np.sqrt(x**2 + y**2))

plt.contour(x, y, z, 25)
plt.show()
