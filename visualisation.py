import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Total balls
total_white = 50
total_black = 50

# Grids
b1_vals = np.arange(0, total_black + 1)
w1_vals = np.arange(0, total_white + 1)
B1, W1 = np.meshgrid(b1_vals, w1_vals)

# Function: probability of drawing a white ball
def compute_white_prob(b1, w1):
    n1 = b1 + w1
    if n1 == 0 or (100 - n1) == 0:
        return np.nan
    b2 = total_black - b1
    w2 = total_white - w1
    p1 = w1 / n1
    p2 = w2 / (w2 + b2)
    return 0.5 * (p1 + p2)

# Compute surface
P_white = np.vectorize(compute_white_prob)(B1, W1)

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(B1, W1, P_white, cmap='plasma')

ax.set_xlabel('b1 (boules noires dans S1)')
ax.set_ylabel('w1 (boules blanches dans S1)')
ax.set_zlabel('Probabilité de tirer une blanche')
ax.set_title('Surface de probabilité pour tirer une blanche')

plt.tight_layout()
plt.show()
