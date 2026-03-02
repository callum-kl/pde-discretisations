import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter


L = 1.0
n = 100
dx = L / n
x = np.arange(0.0, L, dx)

un_0 = 0.0 * x
un_0[np.where(x < 0.5)] = 1

c = 1
a = 1
dt = dx * (c / a)

un_1 = un_0 - c * (un_0 - np.roll(un_0, 1))

t = 0
tmax = 2.0

# --- set up figure ---
fig, ax = plt.subplots()
(line,) = ax.plot(x, un_0)
ax.set_xlim(0, L)
ax.set_ylim(-0.2, 1.2)
ax.set_xlabel("x")
ax.set_ylabel("u")

writer = PillowWriter(fps=30)

norms = [np.linalg.norm(un_0), np.linalg.norm(un_1)]
with writer.saving(fig, "pde-discretisations/group_4/visual/leapfrog.gif", dpi=100):
    # write initial frame
    ax.set_title(f"Leapfrog at t={t:.2f}")
    writer.grab_frame()

    while t < tmax - dt / 2:
        t += dt
        un_2 = un_0 - c * (np.roll(un_1, -1) - np.roll(un_1, 1))
        un_0 = un_1
        un_1 = un_2
        norms.append(np.linalg.norm(un_2))

        # update plot
        line.set_ydata(un_1)
        ax.set_title(f"Leapfrog at t={t:.2f}")
        writer.grab_frame()

plt.close(fig)

plt.plot(norms)
plt.show()
