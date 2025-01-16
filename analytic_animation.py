import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
L1 = 1.0  # length of the first pendulum (m)
L2 = 0.5  # length of the second pendulum (m)
m1 = 5.0  # mass of the first pendulum (kg)
m2 = 1.0  # mass of the second pendulum (kg)

# Initial conditions
theta1_0 = 5 * np.pi / 180      # initial angle of the first pendulum (rad)
theta2_0 = -10 * np.pi / 180    # initial angle of the second pendulum (rad)
z1_0 = 10.0 * np.pi / 180       # initial angular velocity of the first pendulum (rad/s)
z2_0 = 0.0                      # initial angular velocity of the second pendulum (rad/s)

# inisiasi eigenvalue - eigenvector
max_error = 1E-12     # batas error
a = np.array([[L1 / g,  (m2 * L2)/((m1 + m2) * g)], 
              [L1 / g,  L2 / g]])

# pencarian eigenvalue metode QR
i=0
while abs(a[1,0]) > max_error:
    q, r = np.linalg.qr(a)
    a = np.dot(r, q)
    i += 1

omega_a=1/np.sqrt(a[0,0])
omega_b = 1 / np.sqrt(a[1,1])

# pencarian eigenvector
k_a = L1 / (g * a[0,0] - L2)
k_b = L1 / (g * a[1,1] - L2)

# analytic solution function
A_1a = (k_b * theta1_0 - theta2_0) / (k_b - k_a)
A_1b = (k_a * theta1_0 - theta2_0) / (k_a - k_b)
alpha_b = (k_a * z1_0 - z2_0) / ((k_a - k_b) * A_1b * omega_b)
alpha_a = (k_b * z1_0 - z2_0) / ((k_b - k_a) * A_1a * omega_a)
def analytic_theta1(t):
    c_a = np.cos(omega_a * t)
    s_a = np.sin(omega_a * t)
    c_b = np.cos(omega_b * t)
    s_b = np.sin(omega_b * t)
    return A_1a * (c_a + alpha_a * s_a) + A_1b * (c_b + alpha_b * s_b)

def analytic_theta2(t):
    c_a = np.cos(omega_a * t)
    s_a = np.sin(omega_a * t)
    c_b = np.cos(omega_b * t)
    s_b = np.sin(omega_b * t)
    return A_1a * k_a * (c_a + alpha_a * s_a) + A_1b * k_b * (c_b + alpha_b * s_b)

# Equations of motion
def equations(t, y):
    theta1, z1, theta2, z2 = y

    delta_theta = theta1 - theta2

    denom1 = L1 * (2 * m1 + m2 - m2 * np.cos(2 * delta_theta))
    denom2 = L2 * (2 * m1 + m2 - m2 * np.cos(2 * delta_theta))

    theta1_dot = z1
    theta2_dot = z2

    z1_dot = (
        -g * (2 * m1 + m2) * np.sin(theta1)
        - m2 * g * np.sin(theta1 - 2 * theta2)
        - 2 * np.sin(delta_theta) * m2 * (L2 * z2**2 + L1 * z1**2 * np.cos(delta_theta))
    ) / denom1

    z2_dot = (
        2 * np.sin(delta_theta)
        * (
            L1 * (m1 + m2) * z1**2
            + g * (m1 + m2) * np.cos(theta1)
            + L2 * m2 * z2**2 * np.cos(delta_theta)
        )
    ) / denom2

    return [theta1_dot, z1_dot, theta2_dot, z2_dot]

# Time span and resolution
t_span = (0, 10)  # time range (s)
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # time points for evaluation

# Solve the system of ODEs
initial_conditions = [theta1_0, z1_0, theta2_0, z2_0]
solution = solve_ivp(equations, t_span, initial_conditions, t_eval=t_eval, method="RK45")

# Extract solutions
t = solution.t
theta1 = solution.y[0]  # theta1
theta2 = solution.y[2]  # theta2

analytic_theta_1 = analytic_theta1(t)
analytic_theta_2 = analytic_theta2(t)

# Calculate Cartesian coordinates
x1 = (L1) * np.sin(theta1)
y1 = -(L1) * np.cos(theta1)
x2 = L1 * np.sin(theta1) + (L2) * np.sin(theta2)
y2 = -L1 * np.cos(theta1) - (L2) * np.cos(theta2)

# Create the figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid()

# Initialize pendulum lines and masses
line1, = ax.plot([], [], 'o-', lw=2, label="Pendulum 1")
line2, = ax.plot([], [], 'o-', lw=2, label="Pendulum 2")

# Initialization function for animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Store the trajectory of both pendulums
trail1_x = []
trail1_y = []
trail2_x = []
trail2_y = []

# Update function for animation with trail effects
def update(frame):
    # Pendulum 1 coordinates
    xdata1 = [0, x1[frame]]
    ydata1 = [0, y1[frame]]

    # Pendulum 2 coordinates
    xdata2 = [x1[frame], x2[frame]]
    ydata2 = [y1[frame], y2[frame]]

    # Update pendulum lines
    line1.set_data(xdata1, ydata1)
    line2.set_data(xdata2, ydata2)

    # Add the current positions of pendulums to their trails
    trail1_x.append(x1[frame])
    trail1_y.append(y1[frame])
    trail2_x.append(x2[frame])
    trail2_y.append(y2[frame])

    # Update trails
    trail1.set_data(trail1_x, trail1_y)
    trail2.set_data(trail2_x, trail2_y)

    return line1, line2, trail1, trail2

# Initialize the trail lines
trail1, = ax.plot([], [], 'b-', lw=1, label="Pendulum 1 Trail")  # Blue trail for Pendulum 1
trail2, = ax.plot([], [], 'r-', lw=1, label="Pendulum 2 Trail")  # Red trail for Pendulum 2

# Adjust axis limits (optional)
ax.set_xlim(-L1 - L2, L1 + L2)
ax.set_ylim(-L1 - L2, L1 + L2)

# Add legend
ax.legend()

# Create and display the animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)
plt.show()
