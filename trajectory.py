import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,5,101)
g = 9.81
v_0 = 20

def calc_x(time, theta):
    x_pos = v_0 * time * np.cos(theta)
    return x_pos

def calc_y(time, theta):
    y_pos = (v_0 * time * np.sin(theta)) - (0.5 * g * time**2)
    return y_pos

for deg in (30, 45, 60):
    
    rad = (np.pi / 180) * deg
    xs = calc_x(time, rad)
    ys = calc_y(time, rad)

    idx = 0
    for i, y in enumerate(ys):
        if y < 0:
            idx = i
            break
    
    plt.plot(xs[:idx], ys[:idx], 'o', label=f'{deg}°')

plt.title('Trajectories. v0 = 20 m/s')
plt.xlabel('distance / m')
plt.ylabel('height / m')
plt.legend()
plt.savefig('trajectory.png')
plt.show()
