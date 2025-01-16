import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
L1 = 1.0  # length of the first pendulum (m)
L2 = 1.0  # length of the second pendulum (m)
m1 = 1.0  # mass of the first pendulum (kg)
m2 = 1.0  # mass of the second pendulum (kg)

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

# Initial conditions
theta1_0 = np.pi / 4  # initial angle of the first pendulum (rad)
theta2_0 = np.pi / 2  # initial angle of the second pendulum (rad)
z1_0 = 0.0            # initial angular velocity of the first pendulum (rad/s)
z2_0 = 0.0            # initial angular velocity of the second pendulum (rad/s)

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

# Calculate Cartesian coordinates
x1 = (L1) * np.sin(theta1)
y1 = -(L1) * np.cos(theta1)
x2 = L1 * np.sin(theta1) + (L2) * np.sin(theta2)
y2 = -L1 * np.cos(theta1) - (L2) * np.cos(theta2)

# Central difference for velocity and acceleration
def central_difference(data, dt):
    velocity = np.zeros_like(data)
    acceleration = np.zeros_like(data)

    for i in range(1, len(data) - 1):
        velocity[i] = (data[i + 1] - data[i - 1]) / (2 * dt)
        acceleration[i] = (data[i + 1] - 2 * data[i] + data[i - 1]) / (dt**2)

    return velocity, acceleration

# Time step (assuming uniform spacing)
dt = t[1] - t[0]

# Compute velocity and acceleration for each coordinate
v_x1, a_x1 = central_difference(x1, dt)
v_y1, a_y1 = central_difference(y1, dt)
v_x2, a_x2 = central_difference(x2, dt)
v_y2, a_y2 = central_difference(y2, dt)

# Compute total velocity and acceleration for each pendulum
v_total1 = np.sqrt(v_x1**2 + v_y1**2)
a_total1 = np.sqrt(a_x1**2 + a_y1**2)
v_total2 = np.sqrt(v_x2**2 + v_y2**2)
a_total2 = np.sqrt(a_x2**2 + a_y2**2)

# Create a DataFrame for the results
data = {
    "Time (s)": t,
    "x1": x1,
    "y1": y1,
    "x2": x2,
    "y2": y2,
    "v_x1": v_x1,
    "v_y1": v_y1,
    "v_x2": v_x2,
    "v_y2": v_y2,
    "a_x1": a_x1,
    "a_y1": a_y1,
    "a_x2": a_x2,
    "a_y2": a_y2,
    "v_total1": v_total1,
    "a_total1": a_total1,
    "v_total2": v_total2,
    "a_total2": a_total2,
}
df = pd.DataFrame(data)

# Print the table
print(df)