import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.*np.pi, 2.*np.pi, 100)
phase = np.arange(0., 2*np.pi, 2*np.pi/3.)
y_n = [np.sin(x + p) for p in phase]

for y in y_n:
    plt.plot(x, y)

legend_text = ['$\phi$ = %.2f' % p
                            for p in phase]
plt.legend(legend_text)
plt.show()
