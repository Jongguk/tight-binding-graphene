import numpy as np
import matplotlib.pyplot as plt

# https://journals.aps.org/rmp/pdf/10.1103/RevModPhys.81.109
# https://www.physics.umd.edu/courses/Phys732/hdrew/spring07/Schoenenberger%20tutorial%20on%20CNT%20bands.pdf
# https://lampz.tugraz.at/~hadley/ss2/lectures18/oct15.pdf
# https://www.weizmann.ac.il/condmat/oreg/sites/condmat.oreg/files/uploads/2015/tutorial_1.pdf
# https://www.physicsforums.com/threads/plotting-band-structure-in-graphene-a-guide-for-scientists.808913/

a = np.linspace(-2, 2, 400)
b = np.linspace(-2, 2, 400)
x, y = np.meshgrid(a, b)
t = 2.7 # Hopping parameter, Unit: eV
t_prime = - 0.1 * t
l = 1.42 # Bond length, Unit: Å
epsilon = 0
fk = 2 * np.cos(np.sqrt(3) * y * l) + 4 * np.cos(np.sqrt(3) * y * l * 0.5) * np.cos(3 * x * l * 0.5)
CB = ( t * np.sqrt(3 + fk) - t_prime * fk) / t
VB = (- t * np.sqrt(3 + fk) - t_prime * fk) / t

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf1 = ax.plot_surface(x, y, CB, cmap='viridis', alpha = 0.9)
surf2 = ax.plot_surface(x, y, VB, cmap='viridis', alpha = 1)

# ax.set_title('Tight-binding method')
# ax.set_xlabel('k [1/Å]')
# ax.set_zlabel('Energy E/t')

# Remove background color
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(False)

ax.view_init(elev=40, azim=25)
plt.savefig('graphene_band_structure.png', dpi=300) 

plt.show()