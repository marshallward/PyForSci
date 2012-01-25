import numpy as np
import matplotlib.pyplot as plt

x_ax = np.linspace(-2., 2., 100)
y_ax = np.linspace(-2., 2., 100)

x, y = np.meshgrid(x_ax, y_ax)
z = (x-0.5) * np.exp(-np.sqrt(x**2 + y**2))

z_ext = (x_ax[0], x_ax[-1], y_ax[0], y_ax[-1])

plt.imshow(z, origin='lower', extent=z_ext)
plt.show()
