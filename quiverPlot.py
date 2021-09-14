"""

A quiver(x,y,u,v) plot displays the velocity vectors as arrows with components (u,v) at the points (x,y). The above command plots vectors as arrows at the coordinates specified in each corresponding pair of elements in x and y.

"""

import matplotlib.pyplot as plt

import numpy as np

plt.style.use("dark_background")

x,y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .25))

z = x*np.exp(-x**2 - y**2)

v, u = np.gradient(z, .2, .2)

fig, ax = plt.subplots()

q = ax.quiver(x,y,u,v, color="yellow")

plt.xticks([])

plt.yticks([])

plt.grid(False)

plt.box(True)

plt.suptitle('A quiver(x,y,u,v) plot displays the velocity vectors as arrows with components (u,v) at the points (x,y)', fontsize=8.6, color="white")

plt.title('Quiver Plot', color="white", fontsize=15)

plt.figtext(0.83, 0.01, "© Mǟɖ↻ôɖɆⱤ™", color="white", fontsize=10)

plt.show()

plt.savefig('plot.png')
