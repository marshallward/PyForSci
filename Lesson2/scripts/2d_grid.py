import numpy as np

x_ax = np.linspace(-1., 1., 11)
y_ax = np.linspace(0., 1., 6)
x, y = np.meshgrid(x_ax, y_ax)

f = np.sin(x) * np.cosh(y)
print f   # grid is (y, x)!
df_x = f[:, 1:] - f[:, :-1]
df_y = f[1:, :] - f[:-1, :]
