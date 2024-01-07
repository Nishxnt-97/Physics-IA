import matplotlib.pyplot as plt
import numpy as np

# Constants
mass = 0.15  # Mass of the pendulum bob in kg
g = 9.81  # Acceleration due to gravity in m/s^2
spring_constant = 120  # Spring constant in N/m
initial_length = 0.19  # Initial length of the pendulum with no spring in meters

# Given data
angles_deg = np.array([30, 40, 50, 60, 70, 80, 90, 100])
lengths_cm = np.array([20.0, 20.5, 21.0, 21.4, 22.1, 22.4, 23.4, 24.4])
lengths_m = lengths_cm / 100  # Convert lengths to meters
extensions_m = lengths_m - initial_length  # Calculate the extension in meters

# Calculate height at different angles using the provided formula
theta_rad = np.radians(angles_deg)  # Convert angles to radians for calculation
heights_m = 0.35 - 0.30 * np.cos(theta_rad)

# Calculate Gravitational Potential Energy (GPE)
gpe = mass * g * heights_m

# Calculate Elastic Potential Energy (EPE) at each angle
epe = 0.5 * spring_constant * extensions_m**2

# Calculate Kinetic Energy (KE) assuming that initially all GPE is converted to EPE and KE
ke = gpe - epe

# Plotting
fig, ax = plt.subplots()

# Create bar graph
bar_width = 0.35
bar_positions = np.arange(len(angles_deg))

# Divide the bar into two colors representing EPE and KE
p1 = ax.bar(bar_positions, epe, bar_width, label='Elastic Potential Energy', color='green')
p2 = ax.bar(bar_positions, ke, bar_width, bottom=epe, label='Kinetic Energy', color='blue')

# Aesthetics
ax.set_xlabel('Angle (Deg)')
ax.set_ylabel('Energy (Joules)')
ax.set_title('Gravitational Potential Energy Conversion at Different Angles')
ax.set_xticks(bar_positions)
ax.set_xticklabels(angles_deg)
ax.legend()

# Show plot
plt.tight_layout()
plt.show()
