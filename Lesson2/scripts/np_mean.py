import numpy as np

N = 1001    # (N-1) intervals
x = np.linspace(-1., 1., N)

print np.mean(np.sin(x))
print np.mean(1/(1 + x**2))
print np.mean(x**2 * np.exp(-x**2))
