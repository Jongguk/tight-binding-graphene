import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5, 2.5, 200)
y = np.linspace(-10, 10, 100)
a, b = np.meshgrid(x, y)
z = 3.033 * np.sqrt(1 + 4 * np.cos(b * 0.1 * np.pi) * np.cos(a * 1.2283) + 4 * (np.cos(a * 1.2283))**2)
zz = -3.033 * np.sqrt(1 + 4 * np.cos(b * 0.1 * np.pi) * np.cos(a * 1.2283) + 4 * (np.cos(a * 1.2283))**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf1 = ax.plot_surface(a, b, z, cmap='viridis')
surf2 = ax.plot_surface(a, b, zz, cmap='viridis')

ax.set_title('Tight-binding method test')
ax.set_xlabel('K(1/A)')
ax.set_zlabel('Energy (eV)')

plt.show()
