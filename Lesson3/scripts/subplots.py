import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.*np.pi, 2.*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(nrows=2,
                               ncols=1)
ax1.plot(x, y1)
ax2.plot(x, y2)

plt.show()
